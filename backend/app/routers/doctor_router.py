from fastapi import APIRouter, HTTPException
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
    if name or len(name.strip()) > 0:
        specializationBR = SpecializationBR()
        return specializationBR.insertSpecialization(name)
    else:
        raise HTTPException(status_code=404, detail = "Name can not be empty")