from enigma_classes.functions import dict_from_str_with_pairs


class Reflector():

    """Represent reflector of machine with two ways dictionary"""

    def __init__(self, name: str, wiring: str) -> None:

        validate_reflector(name, wiring)
        self._name = name
        reflector_dict = dict_from_str_with_pairs(wiring)
        self._reflector_dict = reflector_dict
        self._wiring = wiring

    @property
    def name(self) -> str:

        """Proper name of reflector"""

        return self._name

    @property
    def reflector_dict(self) -> dict:

        """Dictionary use to code letter.
        (for example {'A': 'B'} means that A letter is code to B)
        Dictionary is symmetrical, so if A match to B, B match to A"""

        return self._reflector_dict

    @property
    def wiring(self) -> str:

        """Wiring in string format which is given to constructor
        Useless in coding meaning, but needed to display wiring in GUI"""

        return self._wiring

    def set_name(self, new_name: str) -> None:

        """Set new name to reflector after its validation"""

        validate_reflector(new_name, self.wiring)
        self._name = new_name

    def set_wiring(self, new_wiring: str) -> None:

        """Set new wiring to reflector after its validation
        Generate reflector_dict for given wiring"""

        validate_reflector(self.name, new_wiring)
        reflector_dict = dict_from_str_with_pairs(new_wiring)
        self._reflector_dict = reflector_dict
        self._wiring = new_wiring

    def code(self, ASCII_letter: int) -> int:

        """Code one letter given as a number"""

        return self.reflector_dict[ASCII_letter]


def validate_reflector(name: str, wiring: str) -> None:

    """Check the data passed as Reflector Object property
    name: have to be a string with at least one char
    wiring: have to be a string with all uppercase letters of english alphabet
    grouped in pairs and separated with spaces"""

    # list of allowed signs
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # counter of letters in current group seprate by spaces
    letters_in_group = 0

    # table of lettrs which alreade apear
    check_table = []

    for position, letter in enumerate(wiring, 1):

        # check if letter is a space
        if letter == " ":

            # check, if space apear after group of two signs
            if letters_in_group == 2:

                # if yes, format is ok for now
                letters_in_group = 0
            else:

                # if not, format is invalid
                raise ReflectorInvalidWiringError

        # check if the last group also have two signs
        # (spcial condition because there is no space after it)
        elif position == len(wiring) and letters_in_group != 1:
            raise ReflectorInvalidWiringError

        # check if letter is in alphabet
        # (we have checked the space before so there is no problem with it)
        elif letter not in alphabet:

            # if not that sign is invalid
            raise ReflectorInvalidSignError

        # check if letter is in check table
        # (was there the same letter before?)
        elif letter in check_table:

            # if yes letter is duplicated
            raise ReflectorDuplicatedLetterError

        else:

            # if go here, the format is ok for now
            letters_in_group += 1
            check_table.append(letter)

    # check if all letters ara included
    # when checked that all letters is in alphabet and no one is duplicated
    # that condition is enough
    if len(wiring) != 38:

        raise ReflectorNotAllLettersError

    # check if reflector name is empty
    if len(name) == 0:

        # if yes, that name is not valid
        raise ReflectorEmptyNameError


class ReflectorNotAllLettersError(Exception):
    pass


class ReflectorInvalidWiringError(Exception):
    pass


class ReflectorEmptyNameError(Exception):
    pass


class ReflectorDuplicatedLetterError(Exception):
    pass


class ReflectorInvalidSignError(Exception):
    pass
