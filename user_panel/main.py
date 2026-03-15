from fastapi import FastAPI

from routers.auth_router import router as auth_router
from routers.courses_router import router as courses_router
from routers.enrollment_router import router as enrollment_router
from routers.progress_router import router as progress_router


from routers.plans_router import router as plans_router
from routers.subscription_router import router as subscription_router
from routers.payment_router import router as payment_router


app = FastAPI(title="Learning Management Platform API")

app.include_router(auth_router)
app.include_router(courses_router)
app.include_router(enrollment_router)
app.include_router(progress_router)


app.include_router(plans_router)
app.include_router(subscription_router)
app.include_router(payment_router)