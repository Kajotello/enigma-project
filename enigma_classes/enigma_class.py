from enigma_classes.functions import to_number
from typing import List
from enigma_classes.rotor_class import Rotor
from enigma_classes.reflector_class import Reflector
from enigma_classes.plugboard_class import Plugboard
from enigma_classes.functions import to_letter


class Enigma():

    """Represent Enigma machine with combination of rotors and reflector, and with
    starting configuration - start positions of rotors and rings"""

    def __init__(self, rotors: List[Rotor], reflector: Reflector,
                 plugboard: Plugboard, start_positions: List[str],
                 rings: List[str], double_step=0) -> None:
        self._start_positions = start_positions
        self._rotors = rotors
        self._reflector = reflector
        self._plugboard = plugboard
        self._coded_letters_number = 0
        self._double_step = double_step
        start_positions = [to_number(position) for position in start_positions]
        rings = [to_number(ring) for ring in rings]
        for i, ring in enumerate(rings):
            self.rotors[i].reverse_rotate(ring)
            self.rotors[i].set_ring(ring)
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

    @property
    def coded_letters_number(self):
        return self._coded_letters_number

    @property
    def double_step(self):
        return self._double_step

    def increment_coded_letters_number(self):
        self._coded_letters_number += 1

    def zero_coded_letters_number(self):
        self._coded_letters_number = 0

    def change_double_step(self, new_double_step):
        self._double_step = new_double_step

    def code_letter(self, plain_letter: str):

        """Code one letter with current Enigma configuration """

        if self.double_step == 2:
            self.rotors[-2].rotate()
            self.rotors[-3].rotate()
            self.change_double_step(1)

        # check, is further rotors should be rotate
        for i, rotor in enumerate(reversed(self.rotors), start=1):
            # flag condition prevent from multiple rotate of further rotors
            # when previous is on intendent position
            if(rotor.position == rotor.indentation) and \
              (i != len(self.rotors)) and \
              (rotor.rotate_flag is True):
                if self.double_step == 1 and i == 1:
                    self.rotors[-i-1].rotate()
                    self.change_double_step(2)
                    break
                else:
                    self.rotors[-i-1].set_rotate_flag(False)
                    self.rotors[-i].set_rotate_flag(True)
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

        self.increment_coded_letters_number()

        return (to_letter(ASCII_letter), [to_letter(step) for step in steps])

    def code_file(self, input_file, output_file, space_dist=5):

        """Code given file with current configuration as start
        As result another file is generated"""

        result = ""
        with open(input_file, "r") as file_handle:
            for line in file_handle:
                for i, letter in enumerate(line):
                    result += self.code_letter(letter)[0]
                    if self.coded_letters_number == space_dist:
                        self.zero_coded_letters_number()
                        result += " "

        with open(output_file, "w") as file_handle:
            file_handle.write(result)
