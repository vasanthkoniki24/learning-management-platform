Subscription-Based Video Learning Platform

Project Overview

This project is a Subscription-Based Video Learning Platform built using Django (Admin Panel) and FastAPI (User Panel).
It extends the previous Learning Management System (LMS) by adding subscription plans, payment tracking, and plan-based course access.

The platform simulates a real-world learning system similar to Udemy, Coursera, or Skillshare.

The system is divided into two main parts:

• Django Admin Panel – Used by administrators to manage users, courses, subscription plans, and payments.
• FastAPI Backend APIs – Used by learners and instructors to access courses, manage subscriptions, and view payment history.

Both panels share a common database.

---

Technologies Used

Backend

- Python
- Django (Admin Panel)
- FastAPI (User Panel APIs)
- SQLAlchemy ORM
- SQLite Database

Authentication

- JWT Authentication
- Passlib (Password Hashing)

Frontend (Admin UI)

- Bootstrap
- Chart.js

API Testing

- Swagger UI
- ApiDog
- Postman

---

Project Architecture

Learning Platform

                ┌──────────────────────┐
                │   Django Admin Panel │
                │                      │
                │ Manage Users        │
                │ Manage Courses      │
                │ Manage Plans        │
                │ Manage Payments     │
                └──────────┬──────────┘
                           │
                           │ Shared Database
                           │ (SQLite)
                           │
                ┌──────────▼──────────┐
                │     FastAPI APIs    │
                │                     │
                │ User Authentication │
                │ Course Access       │
                │ Subscription System │
                │ Payment Tracking    │
                └─────────────────────┘

---

Project Structure

learning_platform/

│
├── admin_panel/                 # Django Admin Panel
│   │
│   ├── courses/
│   ├── subscriptions/
│   ├── templates/
│   ├── static/
│   └── manage.py
│
├── user_panel/                  # FastAPI User APIs
│   │
│   ├── routers/
│   │     ├── auth.py
│   │     ├── courses.py
│   │     ├── plans.py
│   │     ├── subscription.py
│   │     ├── payments.py
│   │
│   ├── models.py
│   ├── database.py
│   └── main.py
│
└── db.sqlite3

---

Features

Django Admin Panel

The Admin Panel allows administrators to manage platform data.

User Management

- Create Users
- Manage Instructor and Student roles

Course Management

- Add Courses
- Add Lessons
- Mark courses as Premium or Free

Subscription Management

- Create Subscription Plans
- Set Plan Price
- Set Plan Duration

Payment Management

- Track payments made by users
- View subscription payment history

Dashboard

- View statistics
- Total Users
- Total Courses
- Total Enrollments
- Chart visualization using Chart.js

---

FastAPI User APIs

FastAPI provides backend APIs for learners and instructors.

Authentication APIs

POST /auth/register
POST /auth/login

Users can register and login using JWT authentication.

---

Plans API

GET /plans

Returns available subscription plans.

Example Response:

[
  {
    "id": 1,
    "name": "Basic",
    "price": 10,
    "duration_days": 30
  }
]

---

Subscription API

POST /subscribe

Users can subscribe to a plan.

Example Request:

user_id = 1
plan_id = 1

This creates:

• Subscription record
• Payment record

---

Courses API

GET /courses
GET /courses/{course_id}

Course access depends on subscription.

If the user has an active subscription:

• Free courses
• Premium courses

If the user does not have subscription:

• Only free courses

---

Payments API

GET /payments

Returns payment history for the user.

Example Response:

[
 {
   "plan_id": 1,
   "amount": 10,
   "payment_date": "2026-03-13"
 }
]

---

Setup Instructions

1 Clone Repository

git clone <your-github-repository-link>

---

2 Create Virtual Environment

python -m venv venv

---

3 Activate Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

---

4 Install Dependencies

pip install -r requirements.txt

---

Running the Project

Run Django Admin Panel

cd admin_panel
python manage.py runserver

Open:

http://127.0.0.1:8000/admin

---

Run FastAPI Server

cd user_panel
uvicorn main:app --reload --port 8001

Open API documentation:

http://127.0.0.1:8001/docs

---

API Testing

APIs can be tested using:

• Swagger UI
• ApiDog
• Postman

---

Testing Workflow

1 Register User

POST /auth/register

2 Login

POST /auth/login

3 View Plans

GET /plans

4 Subscribe to Plan

POST /subscribe

5 Access Courses

GET /courses

6 View Payment History

GET /payments

---

Deliverables

The project includes:

- Complete Source Code
- GitHub Repository
- README Documentation
- API Testing Collection (ApiDog/Postman)
- Screenshots of Working APIs

---

Conclusion

This project demonstrates a real-world backend architecture for an online learning platform by integrating:

• Django Admin Panel
• FastAPI APIs
• Shared Database
• JWT Authentication
• Subscription-Based Access Control

The system showcases how multiple backend frameworks can work together in a scalable learning platform.