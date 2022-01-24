from typing import List


def to_number(char: str) -> int:

    """Change English Alphabet letter to number from 0 to 25"""

    if len(char) != 1:
        raise InvalidLengthError('Char should be a str with length of 1')
    result = ord(char) - 65
    if result < 0 or result > 25:
        raise LetterCodeOutOfRange('This char cannot be changed into \
                                    proper number')
    return result


def to_letter(int: int) -> str:

    """Change number from 0 to 25 to English Alphabet letter"""

    if int < 0 or int > 25:
        raise LetterCodeOutOfRange('This number cannot be changed into letter')
    return chr(int+65)


def first_to_last(list: List) -> List:

    """Switch element on first position on list to last"""

    if len(list) == 0:
        raise EmptyListError('List to transform cannot be empty')
    element = list.pop(0)
    list.append(element)


def last_to_first(list: List) -> List:

    """Switch element on last position on list to first"""

    if len(list) == 0:
        raise EmptyListError('List to transform cannot be empty')
    element = list.pop()
    list.insert(0, element)


def swap(list: List, index1: int, index2: int) -> List:

    """Swap two elements in list"""

    list[index1], list[index2] = list[index2], list[index1]
    return list


def dict_from_str_with_pairs(str: str) -> dict:

    """Change string with pairs of letter seperated with space
    to two way dictionary"""

    result_dict = {}
    pair = []
    for letter in str:
        if letter == ' ':
            first_letter, second_leter = pair
            first_letter = to_number(first_letter)
            second_leter = to_number(second_leter)
            result_dict[first_letter] = second_leter
            result_dict[second_leter] = first_letter
            pair = []
        else:
            pair.append(letter)
    first_letter, second_leter = pair
    first_letter = to_number(first_letter)
    second_leter = to_number(second_leter)
    result_dict[first_letter] = second_leter
    result_dict[second_leter] = first_letter
    return result_dict


class LetterCodeOutOfRange(Exception):
    pass


class EmptyListError(Exception):
    pass


class InvalidLengthError(Exception):
    pass
