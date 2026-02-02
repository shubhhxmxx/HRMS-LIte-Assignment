# Quick Start Guide - HRMS Lite

## 🎯 For Evaluators

This project is **fully deployed and ready to test**. No local setup required!

### Live Application
- **Frontend URL**: https://hrms-lite-frontend.vercel.app
- **Backend API**: https://hrms-lite-api.onrender.com
- **API Docs**: https://hrms-lite-api.onrender.com/docs

### Test the Application

#### 1. Add Employees
1. Click on "Employees" tab
2. Click "Add Employee" button
3. Fill in the form:
   - Employee ID: `EMP001` (must be unique)
   - Full Name: `John Doe`
   - Email: `john.doe@company.com`
   - Department: `Engineering`
4. Click "Add Employee"

**Try these test employees**:
- EMP001 - Alice Johnson - alice@company.com - Engineering
- EMP002 - Bob Smith - bob@company.com - Marketing
- EMP003 - Carol White - carol@company.com - HR
- EMP004 - David Brown - david@company.com - Finance

#### 2. Mark Attendance
1. Click on "Attendance" tab
2. Click "Mark Attendance" button
3. Select an employee from dropdown
4. Select date (defaults to today)
5. Choose status (Present/Absent)
6. Click "Mark Attendance"

#### 3. View Dashboard
1. Click on "Dashboard" tab
2. See real-time statistics:
   - Total Employees
   - Total Attendance Records
   - Today's Present Count
   - Today's Absent Count

### Features to Test

✅ **Employee Management**
- Add employees with validation
- Search employees by ID, name, email, or department
- Delete employees
- Duplicate prevention (try adding same Employee ID twice)
- Email validation (try invalid email format)

✅ **Attendance Tracking**
- Mark attendance for any date
- Search attendance records
- View attendance history
- Duplicate prevention (try marking attendance twice for same date)

✅ **Dashboard**
- Real-time statistics
- Auto-refresh data

✅ **UI/UX**
- Responsive design (test on mobile)
- Loading states
- Error messages
- Success notifications
- Empty states
- Smooth animations

### API Testing (Optional)

You can also test the API directly using the interactive documentation:

**Visit**: https://hrms-lite-api.onrender.com/docs

#### Sample API Calls

**Create Employee**:
```bash
curl -X POST "https://hrms-lite-api.onrender.com/api/employees" \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "EMP005",
    "full_name": "Eva Martinez",
    "email": "eva@company.com",
    "department": "Design"
  }'
```

**Mark Attendance**:
```bash
curl -X POST "https://hrms-lite-api.onrender.com/api/attendance" \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "EMP001",
    "date": "2026-02-02",
    "status": "Present"
  }'
```

**Get All Employees**:
```bash
curl "https://hrms-lite-api.onrender.com/api/employees"
```

**Get Dashboard Stats**:
```bash
curl "https://hrms-lite-api.onrender.com/api/dashboard/stats"
```

## 🔧 Local Development (Optional)

If you want to run it locally:

### Backend
```bash
cd backend
pip install -r requirements.txt
export MONGODB_URL="mongodb://localhost:27017"  # or use MongoDB Atlas URL
python main.py
```

### Frontend
```bash
cd frontend
# Update API_URL in index.html to http://localhost:8000/api
python -m http.server 8080
# Open http://localhost:8080
```

## 📊 Technical Highlights

### Backend
- ✅ RESTful API design
- ✅ Async MongoDB operations
- ✅ Pydantic validation
- ✅ Proper HTTP status codes
- ✅ Error handling
- ✅ CORS configuration
- ✅ API documentation (FastAPI Swagger)

### Frontend
- ✅ React 18 (no build tools)
- ✅ Professional dark theme design
- ✅ Smooth animations
- ✅ Responsive layout
- ✅ Search functionality
- ✅ Modal forms
- ✅ Loading states
- ✅ Error handling
- ✅ Real-time updates

### Database
- ✅ MongoDB (NoSQL)
- ✅ Proper indexing
- ✅ Data validation
- ✅ Relationship handling

## ⚠️ Important Notes

1. **First Request May Be Slow**: The backend is hosted on Render's free tier, which may spin down after inactivity. The first request might take 30-60 seconds to wake up the server.

2. **Data Persistence**: All data is stored in MongoDB Atlas and persists across sessions.

3. **Validation**: Try these to see error handling:
   - Add employee with duplicate Employee ID
   - Add employee with invalid email
   - Mark attendance twice for same date
   - Delete non-existent employee

## 🎨 Design Philosophy

The UI follows a modern, professional aesthetic:
- **Dark theme** for reduced eye strain
- **Gradient accents** for visual interest
- **Smooth animations** for delightful interactions
- **Clear typography** with Darker Grotesque & IBM Plex Mono
- **Responsive design** that works on all devices
- **Professional spacing** and layout

## 📝 Evaluation Checklist

- [x] Functional employee management (Add, View, Delete)
- [x] Functional attendance tracking (Mark, View)
- [x] RESTful API design
- [x] Database persistence (MongoDB)
- [x] Server-side validation
- [x] Error handling with proper status codes
- [x] Professional UI design
- [x] Responsive layout
- [x] Loading and error states
- [x] Search functionality
- [x] Deployed frontend (Vercel)
- [x] Deployed backend (Render)
- [x] Complete documentation
- [x] GitHub repository

## 🚀 Bonus Features Implemented

- ✅ Search/filter for both employees and attendance
- ✅ Dashboard with real-time statistics
- ✅ Duplicate prevention for attendance
- ✅ Professional animations and transitions
- ✅ Modal forms for better UX
- ✅ Empty states with helpful messages
- ✅ Success/error notifications

## 📧 Questions?

If you have any questions or encounter issues, please check:
1. Live application is working at the URLs above
2. API documentation at /docs endpoint
3. README.md for detailed information

---

**Thank you for reviewing this project! 🙏**
