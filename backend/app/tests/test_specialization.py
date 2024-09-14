import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from businessRules import SpecializationBR


def test_getSpecializations():
    specializationBR = SpecializationBR()
    list = specializationBR.getSpecializations()
    assert len(list) == 0
    
def test_insertSpecialzation():
    specializationNameTest = "Test 1"
    specializationBR = SpecializationBR()
    objSpecialization = specializationBR.insertSpecialization(specializationNameTest)
    objSpecializationTest = specializationBR.getSpecializationById(objSpecialization.id)
    assert objSpecializationTest.specializationName == specializationNameTest
        
