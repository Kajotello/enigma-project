from enigma_classes.reflector_class import Reflector
from enigma_classes.rotor_class import Rotor


class ElementsDatabase():

    """Represents database of available rotors and
    reflectors models for the machine"""

    def __init__(self, elements_data=None) -> None:

        # condition make possible to create empty object,
        # which is helpfull to implement __add__

        self._rotors = {}
        self._reflectors = {}

        if elements_data is not None:

            for rotor in elements_data["rotors"]:

                # create Rotor Object for each data in elements_data
                element = Rotor(rotor["name"], rotor["wiring"],
                                rotor["indentations"])
                self._rotors[element.name] = element

            for reflector in elements_data["reflectors"]:

                # create Rotor Object for each data in elements_data
                element = Reflector(reflector["name"], reflector["wiring"])
                self._reflectors[element.name] = element

    def __add__(self, other):

        # check is keys(names) of rotors in dict unique in two databases
        for key in self.rotors.keys():
            if key in other.rotors.keys():
                raise NotUniqueKeyError

        # check is keys(names) of reflectors in dict unique in two databases
        for key in self.reflectors.keys():
            if key in other.reflectors.keys():
                raise NotUniqueKeyError

        if (isinstance(self, CustomElementsDatabase) and
                isinstance(other, CustomElementsDatabase)):
            result = CustomElementsDatabase(self.connected_database)
        else:
            result = ElementsDatabase()
        result._rotors = {**self.rotors, **other.rotors}
        result._reflectors = {**self.reflectors, **other.reflectors}
        return result

    @property
    def rotors(self) -> dict:

        """Dictionary with available rotors models.
        Rotor's names matches to rotor's objects"""

        return self._rotors

    @property
    def reflectors(self) -> dict:

        """Dictionary with available reflectors models.
        Reflector's names matches to reflector's objects"""

        return self._reflectors


class CustomElementsDatabase(ElementsDatabase):

    """Database that store available custom (definied by user)
    elements of Enigma machine"""

    def __init__(self, connected_database, elements_data=None) -> None:
        super().__init__(elements_data)

        # connected database is a database with default elements
        # name of elements have to be unique also with that database
        self._connected_database = connected_database

        # check unique of rotor's names with default database
        for rotor_name in self.rotors.keys():
            self.check_rotor_key_with_second_database(rotor_name, rotor_name)

        # check unique of reflector's names with default database
        for reflector_name in self.reflectors.keys():
            self.check_reflector_key_with_second_database(
                reflector_name, reflector_name)

    @property
    def connected_database(self):
        return self._connected_database

    def add_rotor(self, name: str, wiring: str,
                  indentations: str, allowed_name=None) -> None:

        """Add new rotor model to custom database"""

        # check if the name is unique
        # allowed name is needed, because function is used
        # when modifing rotor -  allowed name make it possible
        # to make exception for leaving the same name
        self.check_rotor_key_with_second_database(name, allowed_name)

        # if yes create rotor and add to database
        new_element = Rotor(name, wiring, indentations)
        self.rotors[name] = new_element

    def add_reflector(self, name: str, wiring: str, allowed_name=None):

        """Add new reflector model to custom database"""

        # check if the name is unique
        # allowed name is needed, because function is used
        # when modifing reflector - allowed name make it possible
        # to make exception for leaving the same name
        self.check_reflector_key_with_second_database(name, allowed_name)

        # if yes create reflector and add to database
        new_element = Reflector(name, wiring)
        self.reflectors[name] = new_element

    def remove_rotor(self, name):

        """Remove rotor model from custom database"""
        try:
            self.rotors.pop(name)
        except KeyError:
            raise InvalidNameError

    def remove_reflector(self, name):

        """Remove reflector model from custom database"""

        try:
            self.reflectors.pop(name)
        except KeyError:
            raise InvalidNameError

    def modify_reflector(self, old_name: str, name: str, wiring: str):

        """Modify one or more parameters of exisiting reflector model"""

        # check if new name is unique (but it can be the same as old_name)
        self.check_reflector_key_with_second_database(name, old_name)

        # if yes remove previous version of reflector model and add new version
        self.add_reflector(name, wiring, old_name)
        if old_name != name:
            self.remove_reflector(old_name)

    def modify_rotor(self, old_name: str, name: str, wiring: str,
                     indentations: str):

        """Modify one or more parameters of exisiting rotor model"""

        # check if new name is unique (but it can be the same as old_name)
        self.check_rotor_key_with_second_database(name, old_name)

        # if yes remove previous version of rotor model and add new version
        self.add_rotor(name, wiring, indentations, old_name)
        if old_name != name:
            self.remove_rotor(old_name)

    def check_rotor_key_with_second_database(self, key, old_key=None):

        """Check unique of rotor name in this
        database and in connected database"""

        if key in self.rotors.keys() and key != old_key:
            raise NameInUseError
        if (self.connected_database is not None and
                key in self.connected_database.rotors.keys()):
            raise NameInUseError

    def check_reflector_key_with_second_database(self, key, old_key=None):

        """Check unique of reflector name in this
        database and in connected database"""

        if key in self.reflectors.keys() and key != old_key:
            raise NameInUseError
        if (self.connected_database is not None and
                key in self.connected_database.reflectors.keys()):
            raise NameInUseError


class NameInUseError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class NotUniqueKeyError(Exception):
    pass
