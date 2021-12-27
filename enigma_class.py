from functions import to_number
from typing import List
from rotor_class import Rotor
from reflector_class import Reflector
from plugboard_class import Plugboard


class Enigma():

    """Represent Enigma machine with combination of rotors and reflector, and with
    starting configuration - start positions of rotors and rings"""

    def __init__(self, rotors: List[Rotor], reflector: Reflector,
                 plugboard: Plugboard, start_positions: List[str],
                 rings: List[str]) -> None:
        self._start_positions = start_positions
        self._rotors = rotors
        self._reflector = reflector
        self._plugboard = plugboard
        start_positions = [to_number(position) for position in start_positions]
        rings = [to_number(ring) for ring in rings]
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

    @property
    def plugboard(self):
        return self._plugboard

    def code_letter(self, plain_letter: str):

        """Code one letter with current Enigma configuration """

        self.rotors[-1].rotate()                 # rotation of last rotor
        ASCII_letter = to_number(plain_letter)

        # letter "goes" throught plugboard (first time)
        ASCII_letter = self.plugboard.code(ASCII_letter)

        # letter "goes" throught all rotors from last to first
        for rotor in reversed(self.rotors):
            ASCII_letter = rotor.code_in(ASCII_letter)

        # letter "goes" throught reflector
        ASCII_letter = self.reflector.code(ASCII_letter)

        # letter "goes" thorught all rotors once again, from first to last
        for rotor in self.rotors:
            ASCII_letter = rotor.code_out(ASCII_letter)

        # letter "goes" throught plugboard (second time)
        ASCII_letter = self.plugboard.code(ASCII_letter)

        # check, is further rotors should be rotate
        for i, rotor in enumerate(reversed(self.rotors), start=1):
            if (rotor.position == rotor.indentation) and \
               (i != len(self.rotors)):
                self.rotors[-i-1].rotate()
            print(rotor.position)

        return chr(ASCII_letter+65)
