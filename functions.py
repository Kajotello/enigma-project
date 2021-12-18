from typing import List


def to_number(char: str) -> int:
    return ord(char) - 65


def first_to_last(list: List):
    element = list.pop(0)
    list.append(element)


def last_to_first(list: List):
    element = list.pop()
    list.insert(0, element)
