from typing import List
from enigma_classes.functions import to_number, first_to_last
from enigma_classes.functions import last_to_first


class Rotor:

    """Represent one rotor of machine with its wiring and indentation"""

    def __init__(self, name: str, wiring: str, indentation: str) -> None:

        self._name = name
        self._wiring = wiring
        self._indentation = to_number(indentation)

        code_table_in, code_table_out = generate_in_out_tables(wiring)
        self._code_table_in = code_table_in
        self._code_table_out = code_table_out

        self._ring = 0
        self._position = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def wiring(self) -> str:
        return self._wiring

    @property
    def indentation(self) -> str:
        return self._indentation

    @property
    def code_table_in(self) -> List[int]:
        return self._code_table_in

    @property
    def code_table_out(self) -> List[int]:
        return self._code_table_out

    @property
    def ring(self) -> int:
        return self._ring

    @property
    def position(self) -> int:
        return self._position

    def set_name(self, new_name: str) -> None:
        validate_rotor(new_name, self.wiring, self.indentation)
        self._name = new_name

    def set_wiring(self, new_wiring: str) -> None:
        validate_rotor(self.name, new_wiring, self.indentation)
        code_table_in, code_table_out = generate_in_out_tables(new_wiring)
        self._code_table_in = code_table_in
        self._code_table_out = code_table_out
        self._wiring = new_wiring

    # need to be fixed - indentation is a str
    def set_indentation(self, indentation: str) -> None:
        validate_rotor(self.name, self.wiring, indentation)
        self._indentation = indentation

    def zero_postion(self) -> None:
        self._position = 0

    def set_ring(self, new_ring: int) -> None:
        self._ring = new_ring

    def rotate(self, number_of_rotation=1, count=True):

        """Simulate rotation of rotor"""

        if number_of_rotation != 0 and count is True:
            self._position = (self._position+number_of_rotation) % 26
        for i in range(number_of_rotation):
            first_to_last(self.code_table_in)
            first_to_last(self.code_table_out)

    def reverse_rotate(self, number_of_rotation=1):

        """Simulate reversed rotation of rotor - not possible in normal
        usage of machine, but helpful to implement ring functionality
        """

        for i in range(number_of_rotation):
            last_to_first(self.code_table_in)
            last_to_first(self.code_table_out)

    def change_position(self, new_position: str):

        """Change position of rotor to given new_position"""

        new_position = to_number(new_position)
        self.reverse_rotate(self.position)
        self.zero_postion()
        self.rotate(new_position)

    def change_ring(self, new_ring: str):

        """Change ring of rotor to given new_ring"""

        new_ring = to_number(new_ring)
        self.rotate(self.ring, count=False)
        self.reverse_rotate(new_ring)
        self.set_ring(new_ring)

    def code_in(self, ASCII_letter):

        """Code leter in 'in' direction"""

        ASCII_letter += self.code_table_in[ASCII_letter]
        return ASCII_letter % 26

    def code_out(self, ASCII_letter):

        """Code leter in 'out' direction"""

        ASCII_letter += self.code_table_out[ASCII_letter]
        return ASCII_letter % 26


def generate_in_out_tables(wiring):

    """Generate code table in both directions with given wiring"""

    code_table_in = []
    temp_code_dict = {}
    code_table_out = []
    # calculate the "jump" for each position in rotor - in "in" direction
    # prepare dictionary for calculation in oposite direction
    for i, letter in enumerate(wiring):
        result_letter_ASCII = to_number(letter)
        code_table_in.append(result_letter_ASCII - i)
        temp_code_dict[result_letter_ASCII] = i

    # calculate the "jump" for each position in rotor - in "out" direction
    for letter in sorted(temp_code_dict):
        code_table_out.append(temp_code_dict[letter] - letter)
    return code_table_in, code_table_out


def validate_rotor(name, wiring, indentation):

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # need to add indentation check

    check_table = []

    if len(wiring) != 26:
        raise NotAllLettersError

    for letter in wiring:
        if letter not in alphabet:
            raise InvalidSignEroor
        if letter in check_table:
            raise DuplicatedLetterError
        else:
            check_table.append(letter)

    if len(name) == 0:
        raise EmptyNameError


class InvalidRotorWiringError(Exception):
    pass


class InvalidSignEroor(Exception):
    pass


class EmptyNameError(Exception):
    pass


class NotAllLettersError(Exception):
    pass


class DuplicatedLetterError(Exception):
    pass
