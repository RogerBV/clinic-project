import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from businessRules import SpecializationBR


def test_getSpecializations():
    print("test_getSpecializations 1")
    specializationBR = SpecializationBR()
    print("test_getSpecializations 2")
    list = specializationBR.getSpecializations()
    print("test_getSpecializations 3")
    assert len(list) == 0
    
#def test_insertSpecialzation():
#    print("test_insertSpecialzation 1")
#    specializationNameTest = "Test 1"
#    print("test_insertSpecialzation 2")
#    specializationBR = SpecializationBR()
#    print("test_insertSpecialzation 3")
#    objSpecialization = specializationBR.insertSpecialization(specializationNameTest)
#    print("test_insertSpecialzation 4")
#    objSpecializationTest = specializationBR.getSpecializationById(objSpecialization.id)
#    print("test_insertSpecialzation 5")
#    assert objSpecializationTest.specializationName.__eq__(specializationNameTest)
        
