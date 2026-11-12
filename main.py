from fastapi import FastAPI, HTTPException, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

def load():
    with open("patients.json") as f:
        return json.load(f)


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "API to manage patient records"}


@app.get("/view")
def view_data():
    return load()


@app.get("/{name}")
def get_city(
    name: str = Path(..., description="Name of the patient", example="Ananya")
):
    data = load()
    return {"city": data.get(name, {}).get("city", "Not found")}


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")
):
    data = load()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")