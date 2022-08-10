from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, validates

# declarative base class
Base = declarative_base()

class Message(db.Model):
    value = db.Column(db.String(255), primary_key=True)

