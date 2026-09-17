from fastapi import FastAPI
from app.routers import auth_router, tasks_router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")
app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "Task Management API"}