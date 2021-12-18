class Enigma():
    def __init__(self, rotors, reflector, start_positions, rings) -> None:
        self._start_positions = start_positions
        self._rotors = rotors
        self._reflector = reflector
        start_positions = [ord(position)-65 for position in start_positions]
        for i, position in enumerate(start_positions):
            for rotate in range(position):
                self.rotors[i].rotate()

    @property
    def rotors(self):
        return self._rotors

    @property
    def reflector(self):
        return self._reflector

    @property
    def start_positions(self):
        return self._start_positions

    def code_letter(self, plain_letter):
        cipher_letter = ord(plain_letter) - 65
        for rotor in reversed(self.rotors):
            cipher_letter += rotor.code_table_in[cipher_letter]
            if cipher_letter < 0:
                cipher_letter += 26
            cipher_letter = cipher_letter % 26
            print(chr(cipher_letter+65))  # to remove
        cipher_letter = self.reflector.reflector_dict[cipher_letter]
        print(chr(cipher_letter+65))
        for rotor in self.rotors:
            cipher_letter += rotor.code_table_out[cipher_letter]
            if cipher_letter < 0:
                cipher_letter += 26
            cipher_letter = cipher_letter % 26
            print(chr(cipher_letter+65))  # to remove
        return chr(cipher_letter+65)
