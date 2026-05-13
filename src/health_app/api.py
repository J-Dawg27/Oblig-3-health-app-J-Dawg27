from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from .health import Health
from .data import load_data, save_data

app = FastAPI(
    title="BMI Health API",
    version="1.0.0",
    description="API for BMI calculation and health advice"
)


class RecordIn(BaseModel):
    name: str
    weight_kg: float
    height_m: float


class RecordOut(BaseModel):
    name: str
    weight_kg: float
    height_m: float
    bmi: float
    category: str
    ideal_weight: float


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": "Health API"
    }


@app.get("/records", response_model=List[RecordOut])
def get_records():

    records = load_data()

    return records


@app.post("/records", response_model=RecordOut, status_code=201)
def create_record(record: RecordIn):

    person = Health(
        name=record.name,
        weight_kg=record.weight_kg,
        height_m=record.height_m
    )

    new_record = {
        "name": person.name,
        "weight_kg": person.weight_kg,
        "height_m": person.height_m,
        "bmi": person.bmi,
        "category": person.category,
        "ideal_weight": person.get_ideal_weight()
    }

    save_data(new_record)

    return new_record