from fastapi import FastAPI
from routes.student_routes import router


app = FastAPI(
    title="University Student CRUD API",
    description="FastAPI CRUD application for university students",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "University Student CRUD API is running"
    }