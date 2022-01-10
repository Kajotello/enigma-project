from enigma_classes.functions import to_number
from enigma_classes.functions import to_letter
from enigma_classes.rotor_class import Rotor
from enigma_classes.reflector_class import Reflector
from enigma_classes.plugboard_class import Plugboard
from typing import List


class Enigma():

    """Represent Enigma machine with combination of rotors and reflector, and with
    configuration - positions of rotors and rings"""

    def __init__(self, rotors: List[Rotor], reflector: Reflector,
                 plugboard: Plugboard, positions: str,
                 rings: str, double_step: bool) -> None:
        self._positions = positions
        self._rotors = rotors
        self._reflector = reflector
        self._plugboard = plugboard
        self._double_step = double_step
        positions = [to_number(position) for position in positions]
        rings = [to_number(ring) for ring in rings]
        for i, ring in enumerate(rings):
            self.rotors[i].reverse_rotate(ring)
            self.rotors[i].set_ring(ring)
        for i, position in enumerate(positions):
            self.rotors[i].rotate(position)

    @property
    def rotors(self):
        return self._rotors

    @property
    def reflector(self):
        return self._reflector

    @property
    def positions(self):
        return self._positions

    @property
    def plugboard(self):
        return self._plugboard

    @property
    def double_step(self):
        return self._double_step

    def change_double_step(self, new_double_step):
        self._double_step = new_double_step

    def code_letter(self, plain_letter: str):

        """Code one letter with current Enigma configuration """

        # check, is further rotors should be rotate
        for i, rotor in enumerate(reversed(self.rotors), start=1):

            # should_rotate condition prevent from multiple rotate
            # of further rotors when previous is on intendent position
            # but wasn't moved recently
            should_roatate = True
            if i > 1:
                if (self.rotors[-i+1].position !=
                   ((self.rotors[-i+1].indentation + 1) % 26)):
                    should_roatate = False
            if(rotor.position == rotor.indentation) and \
              (i != len(self.rotors)) and \
              (should_roatate is True):
                if self.double_step is True and i == 2:
                    self.rotors[-i].rotate()
                    self.rotors[-i-1].rotate()
                    break
                else:
                    self.rotors[-i-1].rotate()

        self.rotors[-1].rotate()                 # rotation of last rotor
        ASCII_letter = to_number(plain_letter)
        steps = [ASCII_letter]

        # letter "goes" throught plugboard (first time)
        ASCII_letter = self.plugboard.code(ASCII_letter)
        steps.append(ASCII_letter)

        # letter "goes" throught all rotors from last to first
        for rotor in reversed(self.rotors):
            ASCII_letter = rotor.code_in(ASCII_letter)
            steps.append(ASCII_letter)

        # letter "goes" throught reflector
        ASCII_letter = self.reflector.code(ASCII_letter)
        steps.append(ASCII_letter)

        # letter "goes" thorught all rotors once again, from first to last
        for rotor in self.rotors:
            ASCII_letter = rotor.code_out(ASCII_letter)
            steps.append(ASCII_letter)

        # letter "goes" throught plugboard (second time)
        ASCII_letter = self.plugboard.code(ASCII_letter)
        steps.append(ASCII_letter)

        # Add letter as output
        steps.append(ASCII_letter)

        return (to_letter(ASCII_letter), [to_letter(step) for step in steps])

    def code_file(self, input_file, output_file, space_dist=5):

        """Code given file with current configuration as start
        As result another file is generated"""

        result = ""
        coded_letter = 0
        with open(input_file, "r") as file_handle:
            for line in file_handle:
                for i, letter in enumerate(line):
                    result += self.code_letter(letter)[0]
                    coded_letter += 1
                    if coded_letter == space_dist:
                        coded_letter = 0
                        result += " "

        with open(output_file, "w") as file_handle:
            file_handle.write(result)
