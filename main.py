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

@app.get("/")
async def root():
    global counter
    counter += 1
    message_val = counter % 3
    return {"message": messages_list[message_val]}

@app.get("/trains")
async def root():
    global cursor
    cursor.execute("SELECT train_name, train_value from train_properties;")
    record = cursor.fetchall()
    print(record)
    return record
