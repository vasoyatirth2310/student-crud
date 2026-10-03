from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    course: str = Field(..., min_length=2)
    semester: int = Field(..., ge=1, le=8)


class Student(StudentCreate):
    id: int