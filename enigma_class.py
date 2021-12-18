class Enigma():
    def __init__(self, rotors, reflector, start_positions, rings) -> None:
        self._start_positions = start_positions
        self._rotors = rotors
        self._reflector = reflector
        start_positions = [ord(position)-65 for position in start_positions]
        rings = [ord(ring)-65 for ring in rings]
        for i, ring in enumerate(rings):
            self.rotors[i].reverse_rotate(ring)
        for i, position in enumerate(start_positions):
            self.rotors[i].rotate(position)

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
        self.rotors[-1].rotate()
        cipher_letter = ord(plain_letter) - 65
        for rotor in reversed(self.rotors):
            cipher_letter += rotor.code_table_in[cipher_letter]
            if cipher_letter < 0:
                cipher_letter += 26
            cipher_letter = cipher_letter % 26
        cipher_letter = self.reflector.reflector_dict[cipher_letter]

        for rotor in self.rotors:
            cipher_letter += rotor.code_table_out[cipher_letter]
            if cipher_letter < 0:
                cipher_letter += 26
            cipher_letter = cipher_letter % 26

        for i, rotor in enumerate(reversed(self.rotors), start=1):
            print(rotor.position, rotor.indentation)
            if (rotor.position == rotor.indentation) and (i != len(self.rotors)):
                self.rotors[-i-1].rotate()

        return chr(cipher_letter+65)
