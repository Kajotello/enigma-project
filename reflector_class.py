from functions import to_number
from typing import List, Tuple


class Reflector():

    """Represent reflector of machine with two ways dictionary"""

    def __init__(self, reflector) -> None:
        reflector_dict = {}
        for pair in reflector:
            first_letter, second_leter = pair
            first_letter = to_number(first_letter)
            second_leter = to_number(second_leter)
            reflector_dict[first_letter] = second_leter
            reflector_dict[second_leter] = first_letter
        self._reflector_dict = reflector_dict

    @property
    def reflector_dict(self):
        return self._reflector_dict
