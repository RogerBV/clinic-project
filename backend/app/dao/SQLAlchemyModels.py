from .shared.base import base_metadata
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .shared.config import DATABASE_URI

from .entities.Specialization import Specialization
from .entities.Person import Person
from .entities.Doctor import Doctor

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

base_metadata.create_all(engine)