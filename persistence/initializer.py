from entity.idea import Idea
from peewee import SqliteDatabase

def init_db():
    db = SqliteDatabase("ideas.db")

    db.connect()
    db.create_tables([Idea])