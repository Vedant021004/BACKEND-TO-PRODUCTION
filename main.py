
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Patient(BaseModel):
    name: str
    age: int
    query: list[str] = []


# POST - Save patient
@app.post("/patient")
def add_patient(patient: Patient):

    with open("patient.json", "r") as file:
        data = json.load(file)

    data.append(patient.model_dump())

    with open("patient.json", "w") as file:
        json.dump(data, file, indent=4)

    return {"message": "Patient saved successfully"}


# GET - Read patients
@app.get("/patient")
def get_patients():

    with open("patient.json", "r") as file:
        return json.load(file)
