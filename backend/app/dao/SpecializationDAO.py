from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .shared.config import DATABASE_URI
from .SQLAlchemyModels import Specialization

class SpecializationDAO():
    
    def getSpecializations(self):
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        specializations = session.query(Specialization).all()
        session.close()
        return specializations
    
    def insertSpecialization(self, name: str):
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            objSpecialization = Specialization(specializationName = name)
            session.add(objSpecialization)
            session.commit()
            session.refresh(objSpecialization)
        except:
            print("Error inserting data")
        finally:
            session.close()
        return objSpecialization
    
    def getSpecializationById(self, specializationId):
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        objSpecialization = Specialization
        try:
            objSpecialization = session.query(Specialization).filter_by(id == specializationId).first()
        except:
            print("Error getting Specialization register")
        return objSpecialization
            
            
    