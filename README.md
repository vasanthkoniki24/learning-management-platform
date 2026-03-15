Learning Management Platform – Subscription Based Extension

Tech Stack
Django - Admin Panel
FastAPI - User APIs
SQLite - Database

Project Structure
admin_panel - Django Admin
user_panel - FastAPI APIs

Setup Instructions

1. Install dependencies
pip install -r requirements.txt

2. Run Django
cd admin_panel
python manage.py runserver

3. Run FastAPI
cd user_panel
uvicorn main:app --reload --port 8001

Admin Panel
http://127.0.0.1:8000/admin

API Documentation
http://127.0.0.1:8001/docs



This project is an extension of the previously developed Learning Management System (LMS).
The system now supports subscription-based learning, allowing users to purchase plans, access premium courses, and track their payment history.

The application follows a multi-panel architecture using two frameworks integrated with a shared database.

---

Architecture

The system consists of two main components:

Admin Panel – Django

The Django admin panel is used by administrators to manage the platform.
Administrators can manage users, create subscription plans, add courses, and monitor user subscriptions and payments.

User Panel – FastAPI

The FastAPI backend provides REST APIs that allow users to register, authenticate, purchase subscription plans, and access courses based on their subscription status.

Both systems share the same database and operate as a unified platform.

---

Key Features

Admin Panel (Django)

Administrators can:

- Manage users
- Create and manage subscription plans (Basic, Pro, Enterprise)
- Add courses and attach video links
- Mark courses as free or premium
- View user subscriptions
- View payment records

---

User Panel (FastAPI)

Users can:

- Register and login using JWT authentication
- View available subscription plans
- Purchase subscription plans
- View available courses
- Access premium courses only when an active subscription exists
- View their payment history

---

Course Access Logic

Course visibility is controlled by the user's subscription status.

- Users without a subscription can access free courses only
- Users with an active subscription can access both free and premium courses
- If a subscription expires, premium course access is restricted

---

API Endpoints

The FastAPI backend exposes the following endpoints:

- POST /auth/register – Register a new user
- POST /auth/login – Authenticate user and return JWT token
- GET /plans – Retrieve available subscription plans
- POST /subscribe – Purchase a subscription plan
- GET /courses – View available courses (free + premium based on subscription)
- GET /payments – View user payment history

---

Video Learning

Courses include video links added by the administrator through the Django Admin panel.
When course data is returned by the API, the video link can be opened directly in the browser to play the learning content.

---

Project Structure

learning_platform
│
├── admin_panel        # Django Admin Panel
├── user_panel         # FastAPI User APIs
├── db.sqlite3         # Shared database
├── requirements.txt
└── README.md

---

Summary

This project demonstrates how Django and FastAPI can be integrated in a real-world multi-panel architecture.

The platform includes:

- Admin management through Django
- User-facing APIs through FastAPI
- JWT authentication
- Subscription and payment management
- Access control for premium learning content