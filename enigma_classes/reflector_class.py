from enigma_classes.functions import dict_from_str_with_pairs


class Reflector():

    """Represent reflector of machine with two ways dictionary"""

    def __init__(self, name: str, wiring: str) -> None:

        validate_reflector(name, wiring)
        self._name = name
        reflector_dict = dict_from_str_with_pairs(wiring)
        self._reflector_dict = reflector_dict
        self._wiring = wiring

    @property
    def name(self) -> str:
        return self._name

    @property
    def reflector_dict(self) -> dict:
        return self._reflector_dict

    @property
    def wiring(self) -> str:
        return self._wiring

    def set_name(self, new_name: str) -> None:
        validate_reflector(new_name, self.wiring)
        self._name = new_name

    def set_wiring(self, new_wiring: str) -> None:
        validate_reflector(self.name, new_wiring)
        reflector_dict = dict_from_str_with_pairs(new_wiring)
        self._reflector_dict = reflector_dict
        self._wiring = new_wiring

    def code(self, ASCII_letter: int) -> int:
        return self.reflector_dict[ASCII_letter]


def validate_reflector(name: str, wiring: str) -> None:

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    i = 0
    check_table = []

    for position, letter in enumerate(wiring, 1):

        if letter == " ":
            if i == 2:
                i = 0
            else:
                raise InvalidReflectorWiringError

        elif letter not in alphabet:
            raise ReflectorInvalidSignError

        elif letter not in check_table:
            if position == len(wiring) and i != 1:
                raise InvalidReflectorWiringError
            i += 1
            check_table.append(letter)

        else:
            raise ReflectorDuplicatedLetterError

    if len(wiring) != 38:
        raise ReflectorNotAllLettersError

    if len(name) == 0:
        raise ReflectorEmptyNameError


class ReflectorNotAllLettersError(Exception):
    pass


class InvalidReflectorWiringError(Exception):
    pass


class ReflectorEmptyNameError(Exception):
    pass


class ReflectorDuplicatedLetterError(Exception):
    pass


class ReflectorInvalidSignError(Exception):
    pass
