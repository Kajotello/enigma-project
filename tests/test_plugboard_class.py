from enigma_classes.plugboard_class import Plugboard
from enigma_classes.plugboard_class import InvalidSignError
from enigma_classes.plugboard_class import DuplicatedLetterError
from enigma_classes.plugboard_class import InvalidPlugboardFormatError
import pytest


def test_Plugboard_class():
    connections = "AB CD"
    plugboard = Plugboard(connections)
    assert plugboard._connections == {0: 1, 1: 0, 2: 3, 3: 2}
    assert plugboard._connections_str == "AB CD"


def test_invalid_connections():
    connections = "AB C DF"
    with pytest.raises(InvalidPlugboardFormatError):
        Plugboard(connections)


def test_invalid_connections_at_the_end():
    connections = "AB CS D"
    with pytest.raises(InvalidPlugboardFormatError):
        Plugboard(connections)


def test_duplicated_letters():
    connections = "AB DF RE QA"
    with pytest.raises(DuplicatedLetterError):
        Plugboard(connections)


def test_invalid_sign():
    connections = "AS Df"
    with pytest.raises(InvalidSignError):
        Plugboard(connections)


def test_connections():
    connections = "ZA"
    plugboard = Plugboard(connections)
    assert plugboard.connections == {25: 0, 0: 25}


def test_empty_connections():
    connections = ""
    plugboard = Plugboard(connections)
    assert plugboard.connections == {}


def test_connections_str():
    connections = "ZA DF CV"
    plugboard = Plugboard(connections)
    assert plugboard.connections_str == "ZA DF CV"


def test_code_letter_in_connections():
    connections = "ZA DF CV"
    plugboard = Plugboard(connections)
    code_letter = plugboard.code(0)
    assert code_letter == 25


def test_code_letter_not_in_connections():
    connections = "ZA DF CV"
    plugboard = Plugboard(connections)
    code_letter = plugboard.code(1)
    assert code_letter == 1
