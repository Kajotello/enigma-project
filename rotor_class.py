class Rotor:
    def __init__(self, rotor, turnover) -> None:
        code_table_in = []
        temp_code_dict = {}
        code_table_out = []
        for i, letter in enumerate(rotor):
            result_letter_ASCII = ord(letter) - 65
            code_table_in.append(result_letter_ASCII - i)
            temp_code_dict[result_letter_ASCII] = i
        self._code_table_in = code_table_in
        for letter in sorted(temp_code_dict):
            code_table_out.append(temp_code_dict[letter] - letter)
        self._code_table_out = code_table_out
        self._turnover = turnover

    @property
    def code_table_in(self):
        return self._code_table_in

    @property
    def code_table_out(self):
        return self._code_table_out

    @property
    def turnover(self):
        return self._turnover

    def rotate(self, number_of_rotation=1):
        for i in range(number_of_rotation):
            moved_elemnt = self.code_table_in.pop(0)
            self.code_table_in.append(moved_elemnt)
            moved_elemnt = self.code_table_out.pop(0)
            self.code_table_out.append(moved_elemnt)
