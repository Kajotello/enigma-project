from enigma_classes.functions import to_number


class Reflector():

    """Represent reflector of machine with two ways dictionary"""

    def __init__(self, name, wiring) -> None:

        self._name = name

        reflector_dict = {}
        for pair in wiring:
            first_letter, second_leter = pair
            first_letter = to_number(first_letter)
            second_leter = to_number(second_leter)
            reflector_dict[first_letter] = second_leter
            reflector_dict[second_leter] = first_letter
        self._reflector_dict = reflector_dict

    @property
    def name(self):
        return self._name

    @property
    def reflector_dict(self):
        return self._reflector_dict

    def code(self, ASCII_letter):
        return self.reflector_dict[ASCII_letter]
