from ..shared.base import Base
from .common.BaseEntity import BaseEntity
from sqlalchemy import Column, String

class Person(Base, BaseEntity):
    __tablename__="Person"
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    documentNumber = Column(String(8), nullable=False)