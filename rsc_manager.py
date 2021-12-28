from functions import read_from_json, write_to_json
from enigma_class import Enigma
from plugboard_class import Plugboard
from reflector_class import Reflector
from rotor_class import Rotor


def load_to_database(data):

    """Create objects (rotors and reflectors)
    from json data and add them to database"""

    rotors = {rotor["name"]: Rotor(rotor["name"],
                                   rotor["wiring"],
                                   rotor["indentation"])
              for rotor in data["rotors"]}
    reflectors = {reflector["name"]: Reflector(reflector["name"],
                                               reflector["wiring"])
                  for reflector in data["reflectors"]}
    data = ElementsDatabase(rotors, reflectors)
    return data


class ElementsDatabase():

    """Represents database of available rotors and
    reflectors for the machine"""

    def __init__(self, rotors, reflectors) -> None:
        self._rotors = rotors
        self._reflectors = reflectors

    def __add__(self, other):
        rotors = {**self.rotors, **other.rotors}
        reflectors = {**self.reflectors, **other.reflectors}
        return ElementsDatabase(rotors, reflectors)

    @property
    def rotors(self):
        return self._rotors

    @property
    def reflectors(self):
        return self._reflectors


class ConfigManager():

    """Resposible for handling json configuration file -
    reading from it and modifications"""

    def __init__(self, rsc_path) -> None:
        self._path = f"{rsc_path}/config.json"  # path to configuration file
        self._data = read_from_json(f"{rsc_path}/config.json")

    @property
    def path(self):
        return self._path

    @property
    def data(self):
        return self._data

    def change_reflector(self, new_reflector):

        """Change reflector type in configuration file"""

        self._data["reflector"] = new_reflector
        write_to_json(self.path, self.data)

    def add_rotor(self, new_rotor, order):

        """Add rotor on specific position (order) in configuration file"""

        self._data["rotors"].insert(order, new_rotor)
        write_to_json(self.path, self.data)

    def remove_rotor(self, order):

        """Remove rotor on specific position (order) in configuration file"""

        self._data["rotors"].pop(order)
        write_to_json(self.path, self.data)

    def set_rotor_ring(self, order, new_ring):
        pass

    def set_rotor_position(self, order, new_position):
        pass

    def set_config_form_file(self, path):

        """Copy configuration to configuration file from another json file"""

        data = read_from_json(path)
        # validity of data should be checked here
        self._data = data
        write_to_json(self.path, data)

    def get_temp_config_from_file(self, path):

        """Once use a configuration from another json file.
        Helpful to implement parser function"""

        self._data = read_from_json(path)


class CustomManager():

    """Resposible for handling json file with custom
    enigma elements (rotors and reflectors) -
    reading from it and modifications"""

    def __init__(self, rsc_path) -> None:
        self._path = f"{rsc_path}/custom.json"
        self._data = read_from_json(f"{rsc_path}/custom.json")

    @property
    def path(self):
        return self._path

    @property
    def data(self):
        return self._data

    def add_rotor(self, name, wiring, indentation):

        """Add new rotor model to custom json database"""

        new_element = {
            "name": name,
            "wiring": wiring,
            "indentation": indentation
        }
        self._data["rotors"].append(new_element)
        write_to_json(self.path, self.data)

    def add_reflector(self, name, wiring):

        """Add new reflector model to custom json database"""

        new_element = {
            "name": name,
            "wiring": wiring,
        }
        self._data["reflectors"].append(new_element)
        write_to_json(self.path, self.data)

    def remove_rotor(self, position):

        """Remove rotor model from custom json database"""

        pass

    def remove_reflector(self, position):

        """Remove reflector model from custom json database"""

        pass


class ResourcesManager():

    """Global manager - handling all resources json file"""

    def __init__(self, rsc_path) -> None:
        self._default = read_from_json(f"{rsc_path}/default.json")
        self._custom = CustomManager(rsc_path)
        self._conf = ConfigManager(rsc_path)

    @property
    def default(self):
        return self._default

    @property
    def custom(self):
        return self._custom

    @property
    def conf(self):
        return self._conf

    def load_elements(self) -> ElementsDatabase:

        """Load elements both from custom and default database to
        ensure full data of available components"""

        full_data = (load_to_database(self.custom.data) +
                     load_to_database(self.default))
        return full_data

    def initialize_enigma(self):

        """Initialize an instance of enigma class with configuration specified in
        config files"""

        elements = self.load_elements()
        rotors = [elements.rotors[rotor] for rotor in self.conf.data["rotors"]]
        reflector = elements.reflectors[self.conf.data["reflector"]]
        plugboard = Plugboard(self.conf.data["plugboard"])
        start_positions = self.conf.data["start_positions"]
        rings = self.conf.data["rings"]
        enigma = Enigma(rotors, reflector, plugboard, start_positions, rings)
        return enigma
