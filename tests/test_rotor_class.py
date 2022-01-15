from enigma_classes.rotor_class import Rotor


def test_Rotor_class():
    name = "rotorI"
    wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indentation = "G"
    rotor = Rotor(name, wiring, indentation)

    assert rotor._name == "rotorI"
    assert rotor._wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor._indentation == 6
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
    assert rotor.indentations == 6


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
    rotor.set_indentation("F")
    assert rotor.indentations == 'F'


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
