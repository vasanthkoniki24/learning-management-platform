Learning Management Platform

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