from typing import List
import json


def to_number(char: str) -> int:
    return ord(char) - 65


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
