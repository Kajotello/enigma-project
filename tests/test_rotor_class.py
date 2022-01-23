from enigma_classes.rotor_class import Rotor
from enigma_classes.rotor_class import RotorInvalidWiringFormatError
from enigma_classes.rotor_class import RotorWiringInvalidSignEroor
from enigma_classes.rotor_class import RotorIndentationInvalidSignError
from enigma_classes.rotor_class import RotorEmptyNameError
from enigma_classes.rotor_class import RotorWiringNotAllLettersError
from enigma_classes.rotor_class import RotorWiringDuplicatedLetterError
from enigma_classes.rotor_class import RotorIndentationDuplicatedLetterError
from enigma_classes.rotor_class import RotorInvalidIndentationFormatError
from enigma_classes.rotor_class import generate_in_out_tables, validate_rotor


def test_Rotor_class():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentations = "GC"
    rotor = Rotor(name, wiring, indentations)

    assert rotor._name == "rotorI"
    assert rotor._wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor._indentations == [6, 2]
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


def test_Rotor_indentation():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)
    assert rotor.indentations == [6]


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
    pass


def test_rotation_one_rotation():
    pass


def test_rotation_n_rotation():
    pass


def test_negative_rotation():
    pass


def test_revrser_rotation():
    pass


def test_change_position():
    pass


def test_change_ring():
    pass


def test_code_in_without_modulo():
    pass


def test_code_in_with_modulo():
    pass


def test_code_out_without_modulo():
    pass


def test_code_out_with_modulo():
    pass


def test_generate_in_out_table():
    pass


def test_validate_rotor_ok():
    pass


def test_validate_rotor_not_all_letters():
    pass


def test_validate_rotor_invalid_sign():
    pass


def test_validate_rotor_duplicated_letter():
    pass


def test_validate_rotor_empty_name():
    pass


def test_validate_rotor_invalid_indentation():
    pass


def test_validation_rotor_invalid_indentation_sign():
    pass


def test_validation_indentation_duplicated_letter():
    pass
