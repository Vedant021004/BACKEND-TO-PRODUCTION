
from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def load():
    with open("patients.json") as f:
        return json.load(f)


@app.get("/")
def home():
    return {
        "name": "Vedant"
    }


@app.get("/a")
def about():
    return {
        "about": "The company belongs to Vedant Kapil."
    }


@app.get("/b")
def contact():
    return {
        "contact": "You can contact Vedant Kapil through email."
    }


@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {
        "first_number": a,
        "second_number": b,
        "sum": a + b
    }


@app.get("/{id}")
def view_patient(sort_by :str = "age" , order : str =  "asc"):

    data = load()

    if sort_by not in ["name", "age", "bmi", "weight"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order")

    patients = list(data.values())

    return sorted(
        patients,
        key=lambda p: p[sort_by],
        reverse=(order == "desc")
    )