from fastapi import FastAPI
from routers import users, courses, enrollment, progress

app = FastAPI(title="Learning Platform API")

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollment.router)
app.include_router(progress.router)


@app.get("/")
def home():
    return {"message": "Learning Platform API running"}