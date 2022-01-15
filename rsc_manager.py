from enigma_classes.functions import read_from_json, to_letter, write_to_json
from enigma_classes.reflector_class import Reflector
from enigma_classes.rotor_class import Rotor
from enigma_classes.enigma_class import Enigma


class ElementsDatabase():

    """Represents database of available rotors and
    reflectors for the machine"""

    def __init__(self, elements_data=None) -> None:
        if elements_data is not None:
            rotors = {}
            reflectors = {}
            for rotor in elements_data["rotors"]:
                element = Rotor(rotor["name"], rotor["wiring"],
                                rotor["indentation"])
                rotors[element.name] = element
            for reflector in elements_data["reflectors"]:
                element = Reflector(reflector["name"], reflector["wiring"])
                reflectors[element.name] = element
            self._rotors = rotors
            self._reflectors = reflectors

    def __add__(self, other):
        for key in self.rotors.keys():
            if key in other.rotors.keys():
                raise NotUniqueKeyError
        for key in self.reflectors.keys():
            if key in other.reflectors.keys():
                raise NotUniqueKeyError
        result = ElementsDatabase()
        result._rotors = {**self.rotors, **other.rotors}
        result._reflectors = {**self.reflectors, **other.reflectors}
        return result

    @property
    def rotors(self):
        return self._rotors

    @property
    def reflectors(self):
        return self._reflectors

    def add_rotor(self, name, wiring, indentation):

        """Add new rotor model to custom database"""

        if name in self.rotors.keys():
            raise NameInUseError
        new_element = Rotor(name, wiring, indentation)
        self.rotors[name] = new_element

    def add_reflector(self, name, wiring):

        """Add new reflector model to custom database"""

        if name in self.reflectors.keys():
            raise NameInUseError
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

    def modify_reflector(self, old_name, name, wiring):
        if name in self.reflectors.keys() and name != old_name:
            raise NameInUseError
        self.remove_reflector(old_name)
        self.add_reflector(name, wiring)

    def modify_rotor(self, old_name, name, wiring, indentation):
        if name in self.rotors.keys() and name != old_name:
            raise NameInUseError
        self.remove_rotor(old_name)
        self.add_rotor(name, wiring, indentation)


class ResourcesManager():

    """Global manager - handling all resources json file"""

    def __init__(self, rsc_path) -> None:
        self.rsc_path = rsc_path
        custom_path = f"{self.rsc_path}/custom.json"
        default_path = f"{self.rsc_path}/default.json"
        self._default = ElementsDatabase(read_from_json(default_path))
        self._custom = ElementsDatabase(read_from_json(custom_path))
        self._elements = self.connect_data()
        # Am I really need it?
        self._conf = self.get_config()

    @property
    def default(self):
        return self._default

    @property
    def custom(self):
        return self._custom

    @property
    def conf(self):
        return self._conf

    @property
    def elements(self):
        return self._elements

    def get_config(self, config_path=None) -> Enigma:

        """Initialize Enigma with configuration from file"""

        if config_path is None:
            config_path = f"{self.rsc_path}/config.json"
        configuration = read_from_json(config_path)
        return Enigma(configuration, self.elements)

    def set_config(self, enigma_machine: Enigma):

        """Write current Enigma configuration to config file"""

        conf_data = {}
        machine = {}
        settings = {}
        machine["rotors"] = []
        machine["rings"] = ""
        machine["start_positions"] = ""
        for rotor in enigma_machine.rotors:
            machine["rotors"].append(rotor.name)
            machine["rings"] += to_letter(rotor.ring)
            machine["start_positions"] += to_letter(rotor.position)
        machine["reflector"] = enigma_machine.reflector.name
        machine["plugboard"] = enigma_machine.plugboard.connections_str
        settings["double_step"] = enigma_machine.double_step
        settings["space_dist"] = enigma_machine.space_dist

        conf_data["machine"] = machine
        conf_data["settings"] = settings

        config_path = f"{self.rsc_path}/config.json"
        write_to_json(config_path, conf_data)
        self._conf = self.get_config()

    def set_custom_database(self):
        data = {}
        data["rotors"] = [{"name": rotor.name,
                           "wiring": rotor.wiring,
                           "indentation": to_letter(rotor.indentation)}
                          for rotor in self.custom.rotors.values()]
        data["reflectors"] = [{"name": reflector.name,
                               "wiring": reflector.wiring}
                              for reflector in self.custom.reflectors.values()]
        custom_path = f"{self.rsc_path}/custom.json"
        write_to_json(custom_path, data)
        self._elements = self.connect_data()

    def connect_data(self):

        """Return database created by connect custom and default
        database"""

        new_data = self.custom + self.default
        return new_data


class NameInUseError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class NotUniqueKeyError(Exception):
    pass
