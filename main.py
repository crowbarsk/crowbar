import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum
import psycopg2


app = FastAPI()
handler = Mangum(app)
counter = 0
connection = psycopg2.connect(database="postgres", user="postgres", password="Salamandra89+", host="postgres.ctksisewojwq.eu-north-1.rds.amazonaws.com", port=5432)
cursor = connection.cursor()
messages_list = ["Filip's site","Awesome AWS","Posunovanie"] 

class Train(BaseModel):
    train_name: str
    train_value: str

@app.get("/")
async def root():
    global counter
    counter += 1
    message_val = counter % 3
    return {"message": messages_list[message_val]}

@app.get("/trains")
async def get_trains():
    global cursor
    cursor.execute("SELECT train_name, train_value from train_properties;")
    record = cursor.fetchall()
    print(record)
    return record

@app.post("/train")
async def post_train(train: Train):
    global cursor
    print(train)
    cursor.execute("INSERT INTO train_properties(train_name, train_value) VALUES(%s, %s)",(train.train_name, train.train_value))
    connection.commit()
    return "Train saved"
