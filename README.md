# HRMS Lite - Human Resource Management System

A lightweight, modern web-based HR management system for managing employee records and tracking attendance.

## 🚀 Live Demo

- **Frontend**: [https://hrms-lite-frontend.vercel.app](https://hrms-lite-frontend.vercel.app)
- **Backend API**: [https://hrms-lite-api.onrender.com](https://hrms-lite-api.onrender.com)
- **API Documentation**: [https://hrms-lite-api.onrender.com/docs](https://hrms-lite-api.onrender.com/docs)

## 📋 Features

### Employee Management
- Add new employees with unique ID, name, email, and department
- View all employees in a clean, searchable table
- Delete employee records
- Automatic duplicate prevention (Employee ID and Email)
- Email validation

### Attendance Tracking
- Mark daily attendance (Present/Absent)
- View attendance history for all employees
- Prevent duplicate attendance for the same date
- Search and filter attendance records

### Dashboard
- Real-time statistics
- Total employees count
- Total attendance records
- Today's attendance summary

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **Vanilla JavaScript** - No build tools for simplicity
- **CSS3** - Modern, responsive design with animations
- **Google Fonts** - Darker Grotesque & IBM Plex Mono

### Backend
- **FastAPI** - Modern Python web framework
- **Motor** - Async MongoDB driver
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Database
- **MongoDB** - NoSQL database for flexible data storage

### Deployment
- **Vercel** - Frontend hosting
- **Render** - Backend API hosting
- **MongoDB Atlas** - Cloud database

## 📦 Installation & Local Setup

### Prerequisites
- Python 3.9+
- MongoDB (local or Atlas)
- Node.js (optional, for local server)

### Backend Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd hrms-lite/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set environment variables:
```bash
export MONGODB_URL="mongodb://localhost:27017"  # Or your MongoDB Atlas URL
```

5. Run the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd hrms-lite/frontend
```

2. Update the API URL in `index.html` (line 640):
```javascript
const API_URL = 'http://localhost:8000/api';  // For local development
```

3. Serve the frontend:
```bash
# Option 1: Python
python -m http.server 8080

# Option 2: Node.js
npx serve .

# Option 3: Any static file server
```

4. Open `http://localhost:8080` in your browser

## 🔌 API Endpoints

### Employees
- `POST /api/employees` - Create new employee
- `GET /api/employees` - Get all employees
- `GET /api/employees/{employee_id}` - Get specific employee
- `DELETE /api/employees/{employee_id}` - Delete employee

### Attendance
- `POST /api/attendance` - Mark attendance
- `GET /api/attendance` - Get all attendance records
- `GET /api/attendance/employee/{employee_id}` - Get employee attendance
- `GET /api/attendance/stats/{employee_id}` - Get attendance statistics

### Dashboard
- `GET /api/dashboard/stats` - Get dashboard statistics
- `GET /health` - Health check endpoint

## 🎨 Design Highlights

- **Dark Theme**: Professional dark mode interface
- **Animated UI**: Smooth transitions and micro-interactions
- **Responsive**: Works on desktop, tablet, and mobile
- **Loading States**: Clear feedback during operations
- **Error Handling**: User-friendly error messages
- **Empty States**: Helpful messages when no data exists

## 📱 Screenshots

### Dashboard
<img width="1821" height="844" alt="image" src="https://github.com/user-attachments/assets/f824f80e-064d-4dd5-895f-024444c7209f" />


### Employee Management
<img width="1834" height="817" alt="image" src="https://github.com/user-attachments/assets/1d62bb0a-2614-4f18-847f-92a37655c0ca" />

### Attendance Tracking
<img width="1850" height="794" alt="image" src="https://github.com/user-attachments/assets/1b7a032f-f497-4c6e-a63f-471be805b348" />


## 🔒 Security Features

- Server-side validation for all inputs
- Email format validation
- Duplicate prevention
- CORS configuration for API security
- Input sanitization

## ⚡ Performance

- Async database operations
- Optimized API responses
- Minimal frontend dependencies
- Fast loading times
- Efficient data fetching

## 🧪 Testing the Application

### Test Employee Data
```json
{
  "employee_id": "EMP001",
  "full_name": "John Doe",
  "email": "john.doe@company.com",
  "department": "Engineering"
}
```

### Test Attendance Data
```json
{
  "employee_id": "EMP001",
  "date": "2026-02-02",
  "status": "Present"
}
```

## 🚀 Deployment Guide

### Backend (Render)

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**: Add `MONGODB_URL`
4. Deploy

### Frontend (Vercel)

1. Create a new project on Vercel
2. Import your GitHub repository
3. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `frontend`
   - **Build Command**: (leave empty)
   - **Output Directory**: `.`
4. Deploy

### Database (MongoDB Atlas)

1. Create a free cluster on MongoDB Atlas
2. Create database user
3. Whitelist IP addresses (0.0.0.0/0 for all)
4. Get connection string
5. Add to backend environment variables

## 📝 Assumptions & Limitations

### Assumptions
- Single admin user (no authentication required)
- Employee IDs are manually assigned
- Attendance can only be marked once per day per employee
- All dates use ISO format (YYYY-MM-DD)

### Limitations
- No authentication/authorization system
- No role-based access control
- No leave management
- No payroll integration
- No bulk operations
- No data export features
- No email notifications

### Future Enhancements
- User authentication and roles
- Leave management module
- Payroll integration
- Advanced reporting and analytics
- Bulk upload via CSV
- Email notifications
- Mobile app version

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Developer

Created as part of a full-stack development assignment.

## 📧 Support

For issues or questions, please open an issue in the GitHub repository.

---

**Note**: This is a demonstration project designed to showcase full-stack development skills. It is not intended for production use without additional security and feature implementations.
