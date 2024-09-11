from .common.BaseEntity import BaseEntity
from ..shared.base import Base
from sqlalchemy import Column, String

class Specialization(Base, BaseEntity):
    __tablename__ = "Specialization"
    specializationName = Column(String(50), nullable=False)