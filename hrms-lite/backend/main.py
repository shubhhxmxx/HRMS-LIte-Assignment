from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date, datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from enum import Enum

app = FastAPI(title="HRMS Lite API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URL)
db = client.hrms_lite

# Collections
employees_collection = db.employees
attendance_collection = db.attendance

# Enums
class AttendanceStatus(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"

# Pydantic models
class EmployeeCreate(BaseModel):
    employee_id: str = Field(..., min_length=1, description="Unique employee ID")
    full_name: str = Field(..., min_length=1, description="Employee full name")
    email: EmailStr = Field(..., description="Employee email address")
    department: str = Field(..., min_length=1, description="Department name")

class EmployeeResponse(BaseModel):
    id: str
    employee_id: str
    full_name: str
    email: str
    department: str
    created_at: datetime

class AttendanceCreate(BaseModel):
    employee_id: str = Field(..., description="Employee ID")
    date: date = Field(..., description="Attendance date")
    status: AttendanceStatus = Field(..., description="Attendance status")

class AttendanceResponse(BaseModel):
    id: str
    employee_id: str
    full_name: str
    date: date
    status: str
    created_at: datetime

# Helper functions
def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "employee_id": employee["employee_id"],
        "full_name": employee["full_name"],
        "email": employee["email"],
        "department": employee["department"],
        "created_at": employee.get("created_at", datetime.utcnow())
    }

def attendance_helper(attendance, employee_name: str = "") -> dict:
    return {
        "id": str(attendance["_id"]),
        "employee_id": attendance["employee_id"],
        "full_name": employee_name,
        "date": attendance["date"],
        "status": attendance["status"],
        "created_at": attendance.get("created_at", datetime.utcnow())
    }

# Routes
@app.get("/")
async def root():
    return {
        "message": "HRMS Lite API",
        "version": "1.0.0",
        "endpoints": {
            "employees": "/api/employees",
            "attendance": "/api/attendance"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

# Employee endpoints
@app.post("/api/employees", response_model=EmployeeResponse, status_code=201)
async def create_employee(employee: EmployeeCreate):
    # Check if employee_id already exists
    existing = await employees_collection.find_one({"employee_id": employee.employee_id})
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    # Check if email already exists
    existing_email = await employees_collection.find_one({"email": employee.email})
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    employee_dict = employee.dict()
    employee_dict["created_at"] = datetime.utcnow()
    
    result = await employees_collection.insert_one(employee_dict)
    created_employee = await employees_collection.find_one({"_id": result.inserted_id})
    
    return employee_helper(created_employee)

@app.get("/api/employees", response_model=List[EmployeeResponse])
async def get_employees():
    employees = []
    async for employee in employees_collection.find():
        employees.append(employee_helper(employee))
    return employees

@app.get("/api/employees/{employee_id}", response_model=EmployeeResponse)
async def get_employee(employee_id: str):
    employee = await employees_collection.find_one({"employee_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_helper(employee)

@app.delete("/api/employees/{employee_id}", status_code=204)
async def delete_employee(employee_id: str):
    result = await employees_collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Also delete all attendance records for this employee
    await attendance_collection.delete_many({"employee_id": employee_id})
    
    return None

# Attendance endpoints
@app.post("/api/attendance", response_model=AttendanceResponse, status_code=201)
async def mark_attendance(attendance: AttendanceCreate):
    # Verify employee exists
    employee = await employees_collection.find_one({"employee_id": attendance.employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Check if attendance already marked for this date
    existing = await attendance_collection.find_one({
        "employee_id": attendance.employee_id,
        "date": attendance.date.isoformat()
    })
    if existing:
        raise HTTPException(
            status_code=400, 
            detail=f"Attendance already marked for {attendance.date}"
        )
    
    attendance_dict = {
        "employee_id": attendance.employee_id,
        "date": attendance.date.isoformat(),
        "status": attendance.status.value,
        "created_at": datetime.utcnow()
    }
    
    result = await attendance_collection.insert_one(attendance_dict)
    created_attendance = await attendance_collection.find_one({"_id": result.inserted_id})
    
    return attendance_helper(created_attendance, employee["full_name"])

@app.get("/api/attendance", response_model=List[AttendanceResponse])
async def get_all_attendance(date_filter: Optional[str] = None):
    query = {}
    if date_filter:
        query["date"] = date_filter
    
    attendance_records = []
    async for record in attendance_collection.find(query).sort("date", -1):
        employee = await employees_collection.find_one({"employee_id": record["employee_id"]})
        employee_name = employee["full_name"] if employee else "Unknown"
        attendance_records.append(attendance_helper(record, employee_name))
    
    return attendance_records

@app.get("/api/attendance/employee/{employee_id}", response_model=List[AttendanceResponse])
async def get_employee_attendance(employee_id: str):
    employee = await employees_collection.find_one({"employee_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    attendance_records = []
    async for record in attendance_collection.find({"employee_id": employee_id}).sort("date", -1):
        attendance_records.append(attendance_helper(record, employee["full_name"]))
    
    return attendance_records

@app.get("/api/attendance/stats/{employee_id}")
async def get_attendance_stats(employee_id: str):
    employee = await employees_collection.find_one({"employee_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    total_records = await attendance_collection.count_documents({"employee_id": employee_id})
    present_count = await attendance_collection.count_documents({
        "employee_id": employee_id,
        "status": "Present"
    })
    absent_count = await attendance_collection.count_documents({
        "employee_id": employee_id,
        "status": "Absent"
    })
    
    return {
        "employee_id": employee_id,
        "full_name": employee["full_name"],
        "total_days": total_records,
        "present_days": present_count,
        "absent_days": absent_count,
        "attendance_percentage": round((present_count / total_records * 100), 2) if total_records > 0 else 0
    }

@app.get("/api/dashboard/stats")
async def get_dashboard_stats():
    total_employees = await employees_collection.count_documents({})
    total_attendance = await attendance_collection.count_documents({})
    
    # Get today's attendance
    today = date.today().isoformat()
    today_present = await attendance_collection.count_documents({
        "date": today,
        "status": "Present"
    })
    today_absent = await attendance_collection.count_documents({
        "date": today,
        "status": "Absent"
    })
    
    return {
        "total_employees": total_employees,
        "total_attendance_records": total_attendance,
        "today_present": today_present,
        "today_absent": today_absent,
        "today_marked": today_present + today_absent
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
