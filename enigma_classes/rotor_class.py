from typing import List
from enigma_classes.functions import to_number, first_to_last
from enigma_classes.functions import last_to_first


class Rotor:

    """Represent one rotor of machine with its wiring and indentations"""

    def __init__(self, name: str, wiring: str, indentations: str) -> None:

        validate_rotor(name, wiring, indentations)

        self._name = name
        self._wiring = wiring
        indentations_as_number = [to_number(indentation)
                                  for indentation in indentations]
        self._indentations = indentations_as_number
        self._indentations_str = indentations
        code_table_in, code_table_out = generate_in_out_tables(wiring)
        self._code_table_in = code_table_in
        self._code_table_out = code_table_out

        self._ring = 0
        self._position = 0

    @property
    def name(self) -> str:

        """Proper name of rotor"""

        return self._name

    @property
    def wiring(self) -> str:

        """Wiring of rotor in str in format 'ABCD...Z'
        Useless to coding but needed to display property in GUI"""

        return self._wiring

    @property
    def indentations(self) -> List[int]:

        """Positions with indentations (max 2)
        Importatnt to calculate rotate of next rotor when mounted in machine"""

        return self._indentations

    @property
    def indentations_str(self) -> str:

        """Indentations in str in format 'AB'
        Useless to coding but needed to display property in GUI"""

        return self._indentations_str

    @property
    def code_table_in(self) -> List[int]:

        """List with 'jumps' matching each letter
        in direction from input to reflector.
        For example if A is code to D in default position
        the table will began with 3 because 0 (A) + 3 = 3 (D)"""

        return self._code_table_in

    @property
    def code_table_out(self) -> List[int]:

        """List with 'jumps' matching each letter
        in direction from reflector to output.
        For example if D is code to A in default position
        the table will began with 3 because 0 (A) + 3 = 3 (D)
        (reverse direction)"""

        return self._code_table_out

    @property
    def ring(self) -> int:

        """Ring position in rotor"""

        return self._ring

    @property
    def position(self) -> int:

        """Position of rotor"""

        return self._position

    def set_name(self, new_name: str) -> None:

        """Set new rotor name"""

        validate_rotor(new_name, self.wiring, self.indentations_str)

        self._name = new_name

    def set_wiring(self, new_wiring: str) -> None:

        """Set new rotor wiring with generated in/out tables"""

        validate_rotor(self.name, new_wiring, self.indentations_str)

        code_table_in, code_table_out = generate_in_out_tables(new_wiring)

        self._code_table_in = code_table_in
        self._code_table_out = code_table_out
        self._wiring = new_wiring

    def set_indentation(self, indentations: str) -> None:

        """Set new rotor indentations"""

        validate_rotor(self.name, self.wiring, indentations)

        indentations_as_numbers = [to_number(indentation)
                                   for indentation in indentations]

        self._indentations = indentations_as_numbers
        self._indentations_str = indentations

    def zero_postion(self) -> None:

        """Reset position to 0"""

        self._position = 0

    def set_ring(self, new_ring: int) -> None:

        """Set ring to given value"""

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


def generate_in_out_tables(wiring: str):

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


def validate_rotor(name, wiring, indentations: str):

    """Check the data passed as Rotor Object property
    name: have to be a string with at least one char
    wiring: have to be a string with all uppercase letters of english alphabet
    indentation: have to be a str with one/two letters of english alphabet"""

    # list of allowed signs
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # table of lettrs which alreade apear
    check_table = []

    for letter in wiring:

        # check if letter is in alphabet
        if letter not in alphabet:

            # if not wiring is invalid
            raise RotorWiringInvalidSignEroor

        # check if letter is in check_table
        if letter in check_table:

            # if yes letter is duplicated, so the wiring is invalid
            raise RotorWiringDuplicatedLetterError
        else:

            check_table.append(letter)

    # check if wiring is shorter than 26
    # (because we previously check that no letter is duplicated)
    if len(wiring) < 26:

        # if yes not all letters are included, so the wiring is invalid
        raise RotorWiringNotAllLettersError

    # check if name is empty
    if len(name) == 0:

        # if yes it is invalid
        raise RotorEmptyNameError

    for position in indentations:

        # check if position in indentations is in alphabet
        if position not in alphabet:

            # if no intdentation is not valid
            raise RotorIndentationInvalidSignError

    # check if length of indentaions is 1 or 2
    if len(indentations) != 1 and len(indentations) != 2:

        # if not indentation is not valid
        raise RotorInvalidIndentationFormatError

    # if length of indentation is 2 check is the letter different
    if len(indentations) == 2:
        if indentations[0] == indentations[1]:

            # if no indentations is not valid
            raise RotorIndentationDuplicatedLetterError


class RotorInvalidWiringFormatError(Exception):
    pass


class RotorWiringInvalidSignEroor(Exception):
    pass


class RotorEmptyNameError(Exception):
    pass


class RotorWiringNotAllLettersError(Exception):
    pass


class RotorWiringDuplicatedLetterError(Exception):
    pass


class RotorIndentationDuplicatedLetterError(Exception):
    pass


class RotorInvalidIndentationFormatError(Exception):
    pass


class RotorIndentationInvalidSignError(Exception):
    pass
