from fastapi import APIRouter
from dao import SpecializationDAO
from businessRules import SpecializationBR

doctorRouter = APIRouter()

@doctorRouter.get("/getDoctors")
async def getDoctors():
    return []

@doctorRouter.get("/getSpecializations")
async def getSpecializations():
    specializationBR = SpecializationBR()
    return specializationBR.getSpecializations()

@doctorRouter.put("/insertSpecialization")
async def insertSpecialization(name: str):
    specializationDAO = SpecializationDAO()
    return specializationDAO.insertSpecialization(name)