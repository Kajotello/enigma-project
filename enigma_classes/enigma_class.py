from typing import List, Tuple

from enigma_classes.reflector_class import Reflector
from enigma_classes.rotor_class import Rotor
from enigma_classes.functions import to_number, to_letter, swap
from enigma_classes.functions import LetterCodeOutOfRange, InvalidLengthError
from enigma_classes.plugboard_class import Plugboard
from copy import deepcopy


class Enigma():

    """Represent Enigma machine with set of rotors, reflector and plugboard"""

    def __init__(self, conf_data: dict, database) -> None:

        # 'unpack' data from conf_data dictionary
        # format is the same as in config.json file
        try:
            rotors = conf_data["machine"]["rotors"]
            positions = conf_data["machine"]["start_positions"]
            reflector = conf_data["machine"]["reflector"]
            plugboard = conf_data["machine"]["plugboard"]
            rings = conf_data["machine"]["rings"]
            space_dist = conf_data["settings"]["space_dist"]
            double_step = conf_data["settings"]["double_step"]
        except KeyError:
            raise InvalidConfData

        # 'Completing' the machine
        self._rotors = []
        for i, rotor in enumerate(rotors):

            # choosing rotors from database and adding to machine as a deepcopy
            # position and ring are setting according to configuration
            try:
                rotor = deepcopy(database.rotors[rotor])
            except KeyError:
                raise RotorNotInDatabaseError(
                    f'Rotor name {rotor} cannot be solved from database')
            rotor.change_position(positions[i])
            rotor.change_ring(rings[i])
            self._rotors.append(rotor)

        # choosing reflector from database
        try:
            self._reflector = database.reflectors[reflector]
        except KeyError:
            raise ReflectorNotInDatabaseError(
                f'Reflector name {reflector} cannot be solved from database')

        # seting plugboard
        self._plugboard = Plugboard(plugboard)

        # if there are more or less than 3 rotors in the machin double step is
        # automatically disabled. Otherwise is set according to data
        if len(self.rotors) == 3:
            self._double_step = double_step
        else:
            self._double_step = False

        # set the space distance in cipher text
        self._space_dist = space_dist

        # set the counter of cipher letters to 0
        self._letter_counter = 0

        # set the database from which potentially new elements will be add
        self._database = database

    @property
    def rotors(self) -> List[Rotor]:

        """List of rotors mounted into Enigma machine"""

        return self._rotors

    @property
    def reflector(self) -> Reflector:

        """Reflector mounted into Enigma machine"""

        return self._reflector

    @property
    def plugboard(self) -> Plugboard:

        """Plugboard set in Enigma machine"""

        return self._plugboard

    @property
    def double_step(self) -> bool:

        """Flag of double step function
        Only available if three rotors are mounted into machine"""

        return self._double_step

    @property
    def space_dist(self) -> int:

        """Distance between spaces in cipher text.
        0 means text without spaces"""

        return self._space_dist

    @property
    def letter_counter(self) -> int:

        """Counter of coded letter, helpfull to calculate place of space"""

        return self._letter_counter

    @property
    def database(self):

        """Database of potentially new elements"""

        return self._database

    def set_database(self, new_database) -> None:

        """Set new database of elements"""

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

        try:
            self._reflector = self.database.reflectors[new_reflector]
        except KeyError:
            raise ReflectorNotInDatabaseError()

    def change_position(self, index: int, new_pos: str) -> None:

        """Change position of rotor with given index to new_pos """

        self.rotors[index].change_position(new_pos)

    def change_ring(self, index: int, new_ring: str) -> None:

        """Change ring of rotor with given index to new_ring """

        self.rotors[index].change_ring(new_ring)

    def add_rotor(self, new_rotor: str) -> None:

        """Add new rotor with given name from database to
        the end of the machine rotors list"""

        try:
            new_rotor = deepcopy(self.database.rotors[new_rotor])
            self._rotors.append(new_rotor)
        except KeyError:
            raise RotorNotInDatabaseError()

    def remove_rotor(self, index: int) -> None:

        """Remove rotor with given index from machine
        rotors list"""

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

    def code_letter(self, letter: str) -> Tuple[str, List[str]]:

        """Code one letter with current configuration"""

        try:
            letter_as_number = to_number(letter)
        except InvalidLengthError:
            raise InvalidSignToCode
        except LetterCodeOutOfRange:
            raise InvalidSignToCode

        # check if further rotors (other then last one) should rotate
        for i, rotor in enumerate(reversed(self.rotors), start=1):
            if i > 1:
                if (self.rotors[-i+1].position not in
                   [((indentation + 1) % 26) for indentation
                   in self.rotors[-i+1].indentations]):
                    break
            if(rotor.position in rotor.indentations) and \
              (i != len(self.rotors)):
                if self.double_step is True and i == 2:
                    self.rotors[-i].rotate()
                    self.rotors[-i-1].rotate()
                    break
                else:
                    self.rotors[-i-1].rotate()

        # rotation of last rotor which take place every time
        self.rotors[-1].rotate()

        # check if space should be placed in cipher text
        if self.letter_counter < self.space_dist or self._space_dist == 0:
            space = ""
            self._letter_counter += 1
        else:
            space = " "
            self._letter_counter = 1

        steps = [letter_as_number]

        # letter "goes" throught plugboard (first time)
        letter_as_number = self.plugboard.code(letter_as_number)
        steps.append(letter_as_number)

        # letter "goes" throught all rotors from last to first
        for rotor in reversed(self.rotors):
            letter_as_number = rotor.code_in(letter_as_number)
            steps.append(letter_as_number)

        # letter "goes" throught reflector
        letter_as_number = self.reflector.code(letter_as_number)
        steps.append(letter_as_number)

        # letter "goes" thorught all rotors once again, from first to last
        for rotor in self.rotors:
            letter_as_number = rotor.code_out(letter_as_number)
            steps.append(letter_as_number)

        # letter "goes" throught plugboard (second time)
        letter_as_number = self.plugboard.code(letter_as_number)
        steps.append(letter_as_number)

        # Add letter as output to steps
        steps.append(letter_as_number)

        cipher_letter = space + to_letter(letter_as_number)

        return cipher_letter, [to_letter(step) for step in steps]

    def code_file(self, input_file: str, output_file: str) -> None:

        """Code file from given input file to output file"""

        self._letter_counter = 0
        result = ""

        # read text from input file and code it
        with open(input_file, "r") as file_handle:
            for line in file_handle:
                for letter in line:
                    result += self.code_letter(letter)[0]

        # write cipher text to output file
        with open(output_file, "w") as file_handle:
            file_handle.write(result)


class InvalidSpaceDistError(Exception):
    pass


class InvalidDoubleStepError(Exception):
    pass


class ReflectorNotInDatabaseError(Exception):
    pass


class RotorNotInDatabaseError(Exception):
    pass


class InvalidConfData(Exception):
    pass


class InvalidSignToCode(Exception):
    pass
