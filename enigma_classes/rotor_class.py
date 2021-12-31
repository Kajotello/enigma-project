from enigma_classes.functions import to_number, to_letter, first_to_last
from enigma_classes.functions import last_to_first


class Rotor:

    """Represent one rotor of machine with its wiring and turnover"""

    def __init__(self, name: str, wiring: str, indentation: str) -> None:

        self._name = name
        self._ring = None
        # declare auxiliary variables
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

        self._code_table_in = code_table_in
        self._code_table_out = code_table_out

        self._indentation = to_number(indentation)
        self._position = 0
        self._rotate_flag = True

    @property
    def name(self):
        return self._name

    @property
    def ring(self):
        return self._ring

    @property
    def code_table_in(self):
        return self._code_table_in

    @property
    def code_table_out(self):
        return self._code_table_out

    @property
    def indentation(self):
        return self._indentation

    @property
    def position(self):
        return self._position

    @property
    def rotate_flag(self):
        return self._rotate_flag

    def set_ring(self, new_ring):
        self._ring = to_letter(new_ring)

    def set_rotate_flag(self, state):
        self._rotate_flag = state

    def rotate(self, number_of_rotation=1):

        """Simulate rotation of rotor"""

        if number_of_rotation != 0:
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

    def code_in(self, ASCII_letter):
        ASCII_letter += self.code_table_in[ASCII_letter]
        return ASCII_letter % 26

    def code_out(self, ASCII_letter):
        ASCII_letter += self.code_table_out[ASCII_letter]
        return ASCII_letter % 26
