
from fastapi import FastAPI
from pydantic import BaseModel, computed_field
import json

app = FastAPI()


class BMI(BaseModel):
    name: str
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


@app.post("/bmi")
def calculate_bmi(person: BMI):

    with open("bmi_data.json", "r") as file:
        data = json.load(file)

    data.append(person.model_dump())

    with open("bmi_data.json", "w") as file:
        json.dump(data, file, indent=4)

    return {
        "message": "BMI calculated and saved",
        "result": person.model_dump()
    }


@app.get("/bmi")
def get_bmi():

    with open("bmi_data.json", "r") as file:
        return json.load(file)
