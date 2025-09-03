from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class car(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristic

car_store: List[car] = []

@app.post("/cars")
def create_cars(car_payload: List[car]):
    car_store.extend(car_payload)
    car_as_json = []
    for c in car_store:
        car_as_json.append(c.model_dump())
    return JSONResponse(content=car_as_json, status_code=201, media_type="application/json")

