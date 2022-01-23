from enigma_classes.plugboard_class import Plugboard, validate_plugboard
from enigma_classes.plugboard_class import PlugboardInvalidSignError
from enigma_classes.plugboard_class import PlugboardDuplicatedLetterError
from enigma_classes.plugboard_class import PlugboardInvalidFormatError
import pytest


def test_Plugboard_class():
    connections = "AB CD"
    plugboard = Plugboard(connections)
    assert plugboard._plugboard_dict == {0: 1, 1: 0, 2: 3, 3: 2}
    assert plugboard._connections == "AB CD"


def test_validate_plugboard_invalid_connections():
    connections = "AB C DF"
    with pytest.raises(PlugboardInvalidFormatError):
        validate_plugboard(connections)


def test_validate_plugboard_invalid_connections_at_the_end():
    connections = "AB CS D"
    with pytest.raises(PlugboardInvalidFormatError):
        validate_plugboard(connections)


def test_validate_plugboard_duplicated_letters():
    connections = "AB DF RE QA"
    with pytest.raises(PlugboardDuplicatedLetterError):
        validate_plugboard(connections)


def test_validate_plugboard_invalid_sign():
    connections = "AS Df"
    with pytest.raises(PlugboardInvalidSignError):
        validate_plugboard(connections)


def test_connections():
    connections = "ZA"
    plugboard = Plugboard(connections)
    assert plugboard.plugboard_dict == {25: 0, 0: 25}


def test_empty_connections():
    connections = ""
    plugboard = Plugboard(connections)
    assert plugboard.plugboard_dict == {}


def test_connections_str():
    connections = "ZA DF CV"
    plugboard = Plugboard(connections)
    assert plugboard.connections == "ZA DF CV"


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
