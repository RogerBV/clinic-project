from dao.SpecializationDAO import SpecializationDAO
from dao.entities import Specialization

class SpecializationBR():
    
    def getSpecializations(self):
        specializationDAO = SpecializationDAO()
        return specializationDAO.getSpecializations()
    
    def insertSpecialization(self, name: str):
        specializationDAO = SpecializationDAO()
        return specializationDAO.insertSpecialization(name)
    
    def getSpecializationById(self, id):
        specializationDAO = SpecializationDAO()
        return specializationDAO.getSpecializationById(id)
    