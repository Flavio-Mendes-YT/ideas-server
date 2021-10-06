from collections import defaultdict
from peewee import BooleanField, DateTimeField, TextField
from entity.base import BaseModel
from datetime import datetime

class Idea(BaseModel):
    description = TextField()
    date = DateTimeField(default=datetime.now())
    done = BooleanField(default=False)
