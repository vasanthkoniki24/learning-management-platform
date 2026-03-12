Learning Management Platform

Overview

This project implements a Learning Management Platform using:

- Django (Admin Panel)
- FastAPI (User Panel APIs)
- SQLite database
- Chart.js for dashboard analytics
- Postman for API testing

---

Admin Panel (Django)

Features:

- Admin authentication
- Manage users
- Manage courses
- Manage lessons
- Manage enrollments
- Dashboard statistics
- Chart.js report for top enrolled courses

Run Admin Panel

cd admin_panel
python manage.py runserver

Admin URL

http://127.0.0.1:8000/admin

---

User Panel (FastAPI)

Features:

- User registration
- User login
- Browse courses
- Course details
- Enroll in courses
- View enrolled courses
- Track progress
- Update learning progress

Run API server

cd user_panel
uvicorn main:app --reload --port 8001

API Documentation

http://127.0.0.1:8001/docs

---

API Endpoints

POST /users/register
POST /users/login

GET /courses
GET /courses/{id}

POST /courses

POST /enroll
GET /my-courses

POST /progress/update
GET /progress/view

---

API Testing

All APIs were tested using Postman.

Postman collection is included in this project.