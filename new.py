
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str
    marks: float


@app.post("/student")
def create_student(student: Student):

    new_student = student.model_dump()

    with open("students.json", "w") as file:
        json.dump(new_student, file, indent=4)

    return {
        "message": "Student saved successfully",
        "student": new_student
    }
