from enigma_classes.reflector_class import Reflector, validate_reflector
from enigma_classes.reflector_class import ReflectorEmptyNameError
from enigma_classes.reflector_class import ReflectorInvalidSignError
from enigma_classes.reflector_class import ReflectorNotAllLettersError
from enigma_classes.reflector_class import ReflectorDuplicatedLetterError
from enigma_classes.reflector_class import ReflectorInvalidWiringError
import pytest


def test_reflector_class():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    assert reflector._name == "reflectorI"
    assert reflector._wiring == "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    assert reflector._reflector_dict == {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4,
                                         6: 7, 7: 6, 8: 9, 9: 8, 10: 11,
                                         11: 10, 12: 13, 13: 12, 14: 15,
                                         15: 14, 16: 17, 17: 16, 18: 19,
                                         19: 18, 20: 21, 21: 20, 22: 23,
                                         23: 22, 24: 25, 25: 24}


def test_validate_reflector_NotAllLettersError():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX"
    with pytest.raises(ReflectorNotAllLettersError):
        validate_reflector(name, wiring)


def test_validate_reflector_InvalidSignError():
    name = "reflectorI"
    wiring = "AB C] EF GH IJ KL MN OP QR ST UV WX YZ"
    with pytest.raises(ReflectorInvalidSignError):
        validate_reflector(name, wiring)


def test_validate_reflector_InvalidReflectorWiringError():
    name = "reflectorI"
    wiring = "AB CD EFGH IJ KL MN OP QR ST UV WX YZ"
    with pytest.raises(ReflectorInvalidWiringError):
        validate_reflector(name, wiring)


def test_validate_reflector_InvalidReflectorWiringError_at_the_end():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WXYZ"
    with pytest.raises(ReflectorInvalidWiringError):
        validate_reflector(name, wiring)


def test_validate_reflector_DuplicatedLetterError():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ AL MN OP QR ST UV WX YZ"
    with pytest.raises(ReflectorDuplicatedLetterError):
        validate_reflector(name, wiring)


def test_validate_reflector_EmptyNameError():
    name = ""
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    with pytest.raises(ReflectorEmptyNameError):
        validate_reflector(name, wiring)


def test_reflector_name():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    assert reflector.name == "reflectorI"


def test_reflector_wiring():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    assert reflector.wiring == "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"


def test_reflector_reflector_dict():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    assert reflector.reflector_dict == {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4,
                                        6: 7, 7: 6, 8: 9, 9: 8, 10: 11,
                                        11: 10, 12: 13, 13: 12, 14: 15,
                                        15: 14, 16: 17, 17: 16, 18: 19,
                                        19: 18, 20: 21, 21: 20, 22: 23,
                                        23: 22, 24: 25, 25: 24}


def test_set_name():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    reflector.set_name("reflectorII")
    assert reflector.name == "reflectorII"
    assert reflector.wiring == "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    assert reflector.reflector_dict == {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4,
                                        6: 7, 7: 6, 8: 9, 9: 8, 10: 11,
                                        11: 10, 12: 13, 13: 12, 14: 15,
                                        15: 14, 16: 17, 17: 16, 18: 19,
                                        19: 18, 20: 21, 21: 20, 22: 23,
                                        23: 22, 24: 25, 25: 24}


def test_set_wiring():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    reflector.set_wiring("AC DB EF GH IJ KL MN OP QR ST UV WX YZ")
    assert reflector.name == "reflectorI"
    assert reflector.wiring == "AC DB EF GH IJ KL MN OP QR ST UV WX YZ"
    assert reflector.reflector_dict == {0: 2, 2: 0, 1: 3, 3: 1, 4: 5, 5: 4,
                                        6: 7, 7: 6, 8: 9, 9: 8, 10: 11,
                                        11: 10, 12: 13, 13: 12, 14: 15,
                                        15: 14, 16: 17, 17: 16, 18: 19,
                                        19: 18, 20: 21, 21: 20, 22: 23,
                                        23: 22, 24: 25, 25: 24}


def test_code():
    name = "reflectorI"
    wiring = "AB CD EF GH IJ KL MN OP QR ST UV WX YZ"
    reflector = Reflector(name, wiring)
    assert reflector.code(7) == 6
