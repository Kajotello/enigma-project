from enigma_classes.functions import to_number


def generate_reflector_dict(wiring):
    reflector_dict = {}
    wiring_str = ""
    for pair in wiring:
        first_letter, second_leter = pair
        wiring_str += first_letter+second_leter+" "
        first_letter = to_number(first_letter)
        second_leter = to_number(second_leter)
        reflector_dict[first_letter] = second_leter
        reflector_dict[second_leter] = first_letter
    return reflector_dict, wiring_str


class Reflector():

    """Represent reflector of machine with two ways dictionary"""

    def __init__(self, name, wiring) -> None:

        self._name = name
        reflector_dict, wiring_str = generate_reflector_dict(wiring)
        self._reflector_dict = reflector_dict
        self._wiring = wiring_str

    @property
    def name(self):
        return self._name

    @property
    def reflector_dict(self):
        return self._reflector_dict

    @property
    def wiring(self):
        return self._wiring

    def __str__(self) -> str:
        return self.wiring

    def set_name(self, new_name):
        self._name = new_name

    def set_wiring(self, new_wiring):
        reflector_dict, wiring_str = generate_reflector_dict(new_wiring)
        self._reflector_dict = reflector_dict
        self._wiring = wiring_str

    def code(self, ASCII_letter):
        return self.reflector_dict[ASCII_letter]
