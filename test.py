
from fastapi import FastAPI

app = FastAPI()

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
