from fastapi import FastAPI

from routers.auth_router import router as auth_router
from routers.courses_router import router as courses_router
from routers.enrollment_router import router as enrollment_router
from routers.progress_router import router as progress_router

app = FastAPI(title="Learning Management Platform API")

app.include_router(auth_router)
app.include_router(courses_router)
app.include_router(enrollment_router)
app.include_router(progress_router)