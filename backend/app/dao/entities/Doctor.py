from ..shared.base import Base
from .common.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, ForeignKey
from .Person import Person
from .Specialization import Specialization


class Doctor(Base, BaseEntity):
    __tablename__="Doctor"
    personId = Column(Integer, ForeignKey('Person.id'), nullable=False)
    specializationId = Column(Integer, ForeignKey('Specialization.id'), nullable=False)