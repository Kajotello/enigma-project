from asyncore import read
from enigma_classes.functions import EmptyListError, WrongPathError, dict_from_str_with_pairs, first_to_last, last_to_first, read_from_json, swap, to_letter, to_number, write_to_json
from enigma_classes.functions import LetterCodeOutOfRange
from enigma_classes.functions import InvalidLengthError
import pytest


def test_to_number():
    char = "A"
    assert to_number(char) == 0


def test_to_number2():
    char = "R"
    assert to_number(char) == 17


def test_to_number_wrong_sign():
    char = '['
    with pytest.raises(LetterCodeOutOfRange):
        to_number(char)


def test_to_number_too_long():
    char = 'AS'
    with pytest.raises(InvalidLengthError):
        to_number(char)


def test_to_number_too_short():
    char = ''
    with pytest.raises(InvalidLengthError):
        to_number(char)


def test_to_letter():
    int = 5
    assert to_letter(int) == "F"


def test_to_letter2():
    int = 20
    assert to_letter(int) == "U"


def test_to_letter_out_of_range():
    int = 26
    with pytest.raises(LetterCodeOutOfRange):
        to_letter(int)


def test_to_letter_out_of_range2():
    int = -4
    with pytest.raises(LetterCodeOutOfRange):
        to_letter(int)


def test_first_to_last():
    list = [5, 6, 2, 3, 9]
    first_to_last(list)
    assert list == [6, 2, 3, 9, 5]


def test_first_to_last_one_element():
    list = [6]
    first_to_last(list)
    assert list == [6]


def test_first_to_last_empty():
    list = []
    with pytest.raises(EmptyListError):
        first_to_last(list)


def test_last_to_first():
    list = [5, 6, 2, 3, 9]
    last_to_first(list)
    assert list == [9, 5, 6, 2, 3]


def test_last_to_first_one_element():
    list = [6]
    last_to_first(list)
    assert list == [6]


def test_last_to_first_empty():
    list = []
    with pytest.raises(EmptyListError):
        last_to_first(list)


def test_read_from_json():
    assert  1 == 0
    #  @TODO


def test_read_from_json_dir_error():
    with pytest.raises(WrongPathError):
        read_from_json('/home')


def test_read_from_json_not_file():
    with pytest.raises(WrongPathError):
        read_from_json('/home/test.txt')


def test_write_to_json():
    assert  1 == 0
    #  @TODO


def test_write_to_json_dir_error():
    with pytest.raises(WrongPathError):
        write_to_json('/home', {})


def test_swap():
    list = [4, 7, 2, 5, 1, 9]
    swap(list, 3, 5)
    assert list == [4, 7, 2, 9, 1, 5]


def test_swap2():
    list = [4, 7, 2, 5, 1, 9]
    swap(list, 4, 2)
    assert list == [4, 7, 1, 5, 2, 9]


def test_dict_from_str_with_pairs():
    str = "AB CD QP RT"
    dict = dict_from_str_with_pairs(str)
    assert dict == {0: 1, 1: 0, 2: 3, 3: 2,
                    16: 15, 15: 16, 17: 19, 19: 17}

