from functions import to_number, first_to_last, last_to_first


class Rotor:

    """Represent one rotor of machine with its wiring and turnover"""

    def __init__(self, rotor: str, indentation: str) -> None:

        # declare auxiliary variables
        code_table_in = []
        temp_code_dict = {}
        code_table_out = []

        # calculate the "jump" for each position in rotor - in "in" direction
        # prepare dictionary for calculation in oposite direction
        for i, letter in enumerate(rotor):
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
