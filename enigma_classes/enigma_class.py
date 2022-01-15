from typing import List
from enigma_classes.rotor_class import Rotor
from enigma_classes.functions import to_number, to_letter, swap
from enigma_classes.plugboard_class import Plugboard
from copy import deepcopy


class Enigma():

    """Represent Enigma machine with set of rotors, reflector and plugboard"""

    def __init__(self, conf_data: dict, database) -> None:

        # enigma is initalized with configuration from config file

        rotors = conf_data["machine"]["rotors"]
        positions = conf_data["machine"]["start_positions"]
        reflector = conf_data["machine"]["reflector"]
        plugboard = conf_data["machine"]["plugboard"]
        rings = conf_data["machine"]["rings"]

        self._rotors = []
        for i, rotor in enumerate(rotors):
            rotor = deepcopy(database.rotors[rotor])
            rotor.change_position(positions[i])
            rotor.change_ring(rings[i])
            self._rotors.append(rotor)

        self._reflector = database.reflectors[reflector]
        self._plugboard = Plugboard(plugboard)
        self._double_step = conf_data["settings"]["double_step"]
        self._space_dist = conf_data["settings"]["space_dist"]
        self._letter_counter = 0
        self._database = database

    @property
    def rotors(self) -> List[Rotor]:
        return self._rotors

    @property
    def reflector(self):
        return self._reflector

    @property
    def plugboard(self):
        return self._plugboard

    @property
    def double_step(self):
        return self._double_step

    @property
    def space_dist(self):
        return self._space_dist

    @property
    def letter_counter(self):
        return self._letter_counter

    @property
    def database(self):
        return self._database

    def update_database(self, new_database) -> None:
        self._database = new_database

    def set_plugboard(self, new_plugboard: str) -> None:

        """Set new plugboard with given connections to machine"""

        self._plugboard = Plugboard(new_plugboard)

    def change_double_step(self) -> None:

        "Negate current state of double step property"

        self._double_step = not self.double_step

    def change_space_dist(self, new_space_dist: int) -> None:

        """Change distance between spaces in encrypted text"""

        self._space_dist = new_space_dist

    def change_reflector(self, new_reflector: str) -> None:

        """Change machine reflector to one with given name from database"""

        self._reflector = self.database.reflectors[new_reflector]

    def change_position(self, index: int, new_pos: str) -> None:

        """Change position of rotor with given index to new_pos """

        self.rotors[index].change_position(new_pos)

    def change_ring(self, index: int, new_ring: str) -> None:

        """Change ring of rotor with given index to new_ring """

        self.rotors[index].change_ring(new_ring)

    def add_rotor(self, new_rotor: str) -> None:

        """Add new rotor with given name from database to
        the end of the machine rotors list"""

        new_rotor = deepcopy(self.database.rotors[new_rotor])
        self._rotors.append(new_rotor)

    def remove_rotor(self, index: int) -> None:

        """Remove rotor with given index from machine
        rotors list"""

        if index is not None:
            self._rotors.pop(index)

    def move_rotor_up(self, index: int) -> None:

        """Move rotor with given index 'up' on the
        machine rotors list"""

        if index != 0:
            self._rotors = swap(self.rotors, index, index-1)

    def move_rotor_down(self, index: int) -> None:

        """Move rotor with given index 'down' on the
        machine rotors list"""

        if index != len(self.rotors)-1:
            self._rotors = swap(self.rotors, index, index+1)

    def code_letter(self, letter: str) -> str:

        """Code one letter with current configuration"""

        for i, rotor in enumerate(reversed(self.rotors), start=1):

            # should_rotate condition prevent from multiple rotate
            # of further rotors when previous is on intendent position
            # but wasn't moved recently
            if i > 1:
                if (self.rotors[-i+1].position !=
                   ((self.rotors[-i+1].indentation + 1) % 26)):
                    break  # not sure about it
            if(rotor.position == rotor.indentation) and \
              (i != len(self.rotors)):
                if self.double_step is True and i == 2:
                    self.rotors[-i].rotate()
                    self.rotors[-i-1].rotate()
                    break
                else:
                    self.rotors[-i-1].rotate()

        self.rotors[-1].rotate()                 # rotation of last rotor

        if self.letter_counter < self.space_dist or self._space_dist == 0:
            space = ""
            self._letter_counter += 1
        else:
            space = " "
            self._letter_counter = 1

        ASCII_letter = to_number(letter)
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

        cipher_letter = space + to_letter(ASCII_letter)

        return cipher_letter, [to_letter(step) for step in steps]

    def code_file(self, input_file: str, output_file: str) -> None:

        """Code file with given starting configuration"""

        self._letter_counter = 0
        result = ""
        with open(input_file, "r") as file_handle:
            for line in file_handle:
                for letter in line:
                    result += self.code_letter(letter)[0]

        with open(output_file, "w") as file_handle:
            file_handle.write(result)
