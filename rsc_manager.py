from enigma_classes.functions import str_change, swap, str_swap_down
from enigma_gui.functions import read_from_json, write_to_json, str_swap_up
from enigma_classes.enigma_class import Enigma
from enigma_classes.plugboard_class import Plugboard
from enigma_classes.reflector_class import Reflector
from enigma_classes.rotor_class import Rotor


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


class Configuration():
    def __init__(self, conf_data) -> None:
        self._rotors = conf_data["rotors"]
        self._reflector = conf_data["reflector"]
        self._positions = conf_data["start_positions"]
        self._rings = conf_data["rings"]
        self._plugboard = conf_data["plugboard"]

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
    def rings(self):
        return self._rings

    @property
    def plugboard(self):
        return self._plugboard

    def add_rotor(self, new_rotor):
        self._rotors.append(new_rotor)
        self._rings += "A"
        self._positions += "A"

    def remove_rotor(self, index):
        self._rotors.pop(index)
        self._rings = str_change(self.rings, index, "")
        self._positions = str_change(self.positions, index, "")

    def change_reflector(self, new_reflector):
        self._reflector = new_reflector

    def change_position(self, index, new_pos):
        self._positions = str_change(self.positions, index, new_pos)

    def change_ring(self, index, new_ring):
        self._rings = str_change(self.positions, index, new_ring)

    def set_plugboard(self, new_plugboard):
        self._plugboard = new_plugboard

    def move_rotor_up(self, index):
        if index != 0:
            self._rotors = swap(self.rotors, index, index-1)
        self._positions = str_swap_up(self.positions, index)
        self._rings = str_swap_up(self.rings, index)

    def move_rotor_down(self, index):
        if index != len(self.rotors)-1:
            self._rotors = swap(self.rotors, index, index+1)
        self._positions = str_swap_down(self.positions, index)
        self._rings = str_swap_down(self.rings, index)

    def save_conf(self, confman):
        confman.set_rotor_positions(self.positions)
        confman.set_rotor_rings(self.rings)
        confman.change_reflector(self.reflector)
        confman.set_new_rotors(self.rotors)
        confman.set_new_plugboard(self.plugboard)


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

    def set_rotor_rings(self, new_rings):
        self._data["rings"] = new_rings
        write_to_json(self.path, self.data)

    def set_rotor_positions(self, new_positions):
        self._data["start_positions"] = new_positions
        write_to_json(self.path, self.data)

    def set_new_rotors(self, new_rotors):
        self._data["rotors"] = new_rotors
        write_to_json(self.path, self.data)

    def set_new_plugboard(self, new_plugboard):
        self._data["plugboard"] = new_plugboard
        write_to_json(self.path, self.data)

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
        self.elements = elements
        rotors = [elements.rotors[rotor] for rotor in self.conf.data["rotors"]]
        reflector = elements.reflectors[self.conf.data["reflector"]]
        plugboard = Plugboard(self.conf.data["plugboard"])
        start_positions = self.conf.data["start_positions"]
        rings = self.conf.data["rings"]
        enigma = Enigma(rotors, reflector, plugboard, start_positions, rings)
        return enigma
