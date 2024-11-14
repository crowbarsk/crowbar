import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
counter = 0
messages_list = ["Filip's site","Awesome AWS","Posunovanie"] 

@app.get("/")
async def root():
    nonlocal counter
    counter += 1
    message_val = counter % 3
    return {"message": messages_list[message_val]}
