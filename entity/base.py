from peewee import *

db = SqliteDatabase("ideas.db")

class BaseModel(Model):
    class Meta:
        database = db