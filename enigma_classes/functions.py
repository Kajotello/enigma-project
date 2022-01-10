from typing import List
import json


def to_number(char: str) -> int:
    return ord(char) - 65


def to_letter(int: int) -> str:
    return chr(int+65)


def first_to_last(list: List):
    element = list.pop(0)
    list.append(element)


def last_to_first(list: List):
    element = list.pop()
    list.insert(0, element)


def read_from_json(path):
    with open(path) as file:
        return json.load(file)


def write_to_json(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def str_change(str, index, new_char):

    """Change string's char with given index to new_char"""

    result = ""
    for i, char in enumerate(str):
        if i == index:
            result += new_char
        else:
            result += char
    return result


def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list


def str_swap_up(str, index):

    """Swap two chars in string (char with given index and one before).
    Char with given index go 'up' in string"""

    if index == 0:
        return str
    str_table = [char for char in str]
    str_table = swap(str_table, index, index-1)
    result = ""
    for element in str_table:
        result += element
    return result


def str_swap_down(str, index):

    """Swap two chars in string (char with given index and one after).
    Char with given index go 'down' in string"""

    if index == len(str) - 1:
        return str
    str_table = [char for char in str]
    str_table = swap(str_table, index, index+1)
    result = ""
    for element in str_table:
        result += element
    return result


def dict_from_str_with_pairs(str):

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
