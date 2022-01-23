import pytest
from enigma_classes.rotor_class import Rotor
from enigma_classes.rotor_class import RotorWiringInvalidSignEroor
from enigma_classes.rotor_class import RotorIndentationInvalidSignError
from enigma_classes.rotor_class import RotorEmptyNameError
from enigma_classes.rotor_class import RotorWiringNotAllLettersError
from enigma_classes.rotor_class import RotorWiringDuplicatedLetterError
from enigma_classes.rotor_class import RotorIndentationDuplicatedLetterError
from enigma_classes.rotor_class import RotorInvalidIndentationFormatError
from enigma_classes.rotor_class import NegativeRotationError
from enigma_classes.rotor_class import generate_in_out_tables, validate_rotor


def test_Rotor_class():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = "GC"
    rotor = Rotor(name, wiring, indentations)

    assert rotor._name == "rotorI"
    assert rotor._wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor._indentations == [6, 2]
    assert rotor._indentations_str == "GC"
    assert rotor._code_table_in == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert rotor.code_table_out == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert rotor._ring == 0
    assert rotor._position == 0


def test_Rotor_name():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.name == "rotorI"


def test_Rotor_wiring():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_Rotor_indentations():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "GY"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.indentations == [6, 24]


def test_Rotor_indenatations_str():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "Y"
    rotor = Rotor(name, wiring, indentation)
    assert rotor._indentations_str == "Y"


def test_Rotor_code_table_in():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.code_table_in == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_Rotor_code_table_out():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.code_table_out == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_Rotor_ring():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.ring == 0


def test_Rotor_position():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.position == 0


def test_set_name():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.set_name('rotorII')
    assert rotor.name == 'rotorII'


def test_set_wiring():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.set_wiring('BCDEFGHIJKLMNOPQRSTUVWXYZA')
    assert rotor.wiring == 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
    assert rotor.code_table_in == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -25]
    assert rotor.code_table_out == [25, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                                    -1, -1, -1, -1]


def test_set_indentation():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.set_indentation("A")
    assert rotor.indentations == [0]


def test_zero_position():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor._position = 5
    rotor.zero_postion()
    assert rotor.position == 0


def test_set_ring():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.set_ring(5)
    assert rotor.ring == 5


def test_rotate_zero_rotation():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.rotate(0)
    assert rotor.position == 0
    assert rotor.code_table_in == [4, 9, 10, 2, 7, 1, -3, 9, 13,  16, 3, 8, 2,
                                   9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6,
                                   -22, -16]
    assert rotor.code_table_out == [20, 21, 22, 3, -4, -2, -1, 8, 13, 16,
                                    -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                                    -3, -13, -9, -7, -10, -16]


def test_rotation_one_rotation():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.rotate()
    assert rotor.position == 1
    assert rotor.code_table_in == [9, 10, 2, 7, 1, -3, 9, 13,  16, 3, 8, 2,
                                   9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6,
                                   -22, -16, 4]
    assert rotor.code_table_out == [21, 22, 3, -4, -2, -1, 8, 13, 16,
                                    -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                                    -3, -13, -9, -7, -10, -16, 20]


def test_rotation_n_rotation():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.rotate(5)
    assert rotor.position == 5
    assert rotor.code_table_in == [1, -3, 9, 13,  16, 3, 8, 2,
                                   9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6,
                                   -22, -16, 4, 9, 10, 2, 7]
    assert rotor.code_table_out == [-2, -1, 8, 13, 16, -9, -7, -10, -3, -2,
                                    4, -9, 6, 0, -8, -3, -13, -9, -7, -10,
                                    -16, 20, 21, 22, 3, -4]


def test_negative_rotation():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    with pytest.raises(NegativeRotationError):
        rotor.rotate(-5)


def test_reverse_one_rotation():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.reverse_rotate()
    assert rotor.position == 0
    assert rotor.code_table_in == [-16, 4, 9, 10, 2, 7, 1, -3, 9, 13,
                                   16, 3, 8, 2, 9, 10, -8, 7, 3, 0,
                                   -4, -20, -13, -21, -6, -22]
    assert rotor.code_table_out == [-16, 20, 21, 22, 3, -4, -2, -1, 8, 13, 16,
                                    -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                                    -3, -13, -9, -7, -10]


def test_revrse_rotation_negative_error():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    with pytest.raises(NegativeRotationError):
        rotor.reverse_rotate(-5)


def test_change_position():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_position('C')
    assert rotor.position == 2
    assert rotor.ring == 0
    assert rotor.code_table_in == [10, 2, 7, 1, -3, 9, 13,  16, 3, 8, 2,
                                   9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6,
                                   -22, -16, 4, 9]
    assert rotor.code_table_out == [22, 3, -4, -2, -1, 8, 13, 16,
                                    -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                                    -3, -13, -9, -7, -10, -16, 20, 21]


def test_change_position_from_not_default():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.rotate(20)
    rotor.change_position('B')
    assert rotor.ring == 0
    assert rotor.position == 1
    assert rotor.code_table_in == [9, 10, 2, 7, 1, -3, 9, 13,  16, 3, 8, 2,
                                   9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6,
                                   -22, -16, 4]
    assert rotor.code_table_out == [21, 22, 3, -4, -2, -1, 8, 13, 16,
                                    -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                                    -3, -13, -9, -7, -10, -16, 20]


def test_change_ring():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_ring('B')
    assert rotor.ring == 1
    assert rotor.position == 0
    assert rotor.code_table_in == [-16, 4, 9, 10, 2, 7, 1, -3, 9, 13,  16, 3,
                                   8, 2, 9, 10, -8, 7, 3, 0, -4, -20, -13,
                                   -21, -6, -22]
    assert rotor.code_table_out == [-16, 20, 21, 22, 3, -4, -2, -1, 8, 13, 16,
                                    -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                                    -3, -13, -9, -7, -10]


def test_change_ring_second_time():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_ring('B')
    rotor.change_ring('D')
    assert rotor.ring == 3
    assert rotor.position == 0
    assert rotor.code_table_in == [-6, -22, -16, 4, 9, 10, 2, 7, 1, -3, 9, 13,
                                   16, 3, 8, 2, 9, 10, -8, 7, 3, 0, -4, -20,
                                   -13, -21]
    assert rotor.code_table_out == [-7, -10, -16, 20, 21, 22, 3, -4, -2, -1,
                                    8, 13, 16, -9, -7, -10, -3, -2, 4, -9,
                                    6, 0, -8, -3, -13, -9]


def test_change_ring_with_set_position():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_position('Z')
    rotor.change_ring('B')
    assert rotor.ring == 1
    assert rotor.position == 25
    assert rotor.code_table_in == [-22, -16, 4, 9, 10, 2, 7, 1, -3, 9, 13,
                                   16, 3, 8, 2, 9, 10, -8, 7, 3, 0, -4,
                                   -20, -13, -21, -6]
    assert rotor.code_table_out == [-10, -16, 20, 21, 22, 3, -4, -2, -1, 8,
                                    13, 16, -9, -7, -10, -3, -2, 4, -9, 6,
                                    0, -8, -3, -13, -9, -7, ]


def test_code_in():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.code_in(2) == 12


def test_code_in_with_ring_change():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_ring('C')
    assert rotor.code_in(3) == 12


def test_code_in_with_position_change():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_position('C')
    assert rotor.code_in(25) == 8


def test_code_out():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.code_out(5) == 3


def test_code_out_with_ring_change():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_ring("B")
    assert rotor.code_out(0) == 10


def test_code_out_with_position_change():
    name = "rotorI"
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    rotor.change_position('C')
    assert rotor.code_out(0) == 22


def test_generate_in_out_table():
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    table_in, table_out = generate_in_out_tables(wiring)
    assert table_in == [4, 9, 10, 2, 7, 1, -3, 9, 13,  16, 3, 8, 2,
                        9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6,
                        -22, -16]
    assert table_out == [20, 21, 22, 3, -4, -2, -1, 8, 13, 16,
                         -9, -7, -10, -3, -2, 4, -9, 6, 0, -8,
                         -3, -13, -9, -7, -10, -16]


def test_validate_rotor_not_all_letters():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    indentations = "GC"
    with pytest.raises(RotorWiringNotAllLettersError):
        validate_rotor(name, wiring, indentations)


def test_validate_rotor_invalid_sign():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRStUVWXYZ"
    indentations = "GC"
    with pytest.raises(RotorWiringInvalidSignEroor):
        validate_rotor(name, wiring, indentations)


def test_validate_rotor_duplicated_letter():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXZZ"
    indentations = "GC"
    with pytest.raises(RotorWiringDuplicatedLetterError):
        validate_rotor(name, wiring, indentations)


def test_validate_rotor_empty_name():
    name = ""
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = "GC"
    with pytest.raises(RotorEmptyNameError):
        validate_rotor(name, wiring, indentations)


def test_validate_rotor_invalid_indentation_too_long():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = "GCP"
    with pytest.raises(RotorInvalidIndentationFormatError):
        validate_rotor(name, wiring, indentations)


def test_validate_rotor_invalid_indentation_too_short():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = ""
    with pytest.raises(RotorInvalidIndentationFormatError):
        validate_rotor(name, wiring, indentations)


def test_validation_rotor_invalid_indentation_sign():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = "a"
    with pytest.raises(RotorIndentationInvalidSignError):
        validate_rotor(name, wiring, indentations)


def test_validation_indentation_duplicated_letter():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = "AA"
    with pytest.raises(RotorIndentationDuplicatedLetterError):
        validate_rotor(name, wiring, indentations)
