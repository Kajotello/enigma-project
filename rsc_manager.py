from enigma_classes.functions import str_change, swap, str_swap_down
from enigma_gui.functions import read_from_json, write_to_json, str_swap_up
from enigma_classes.enigma_class import Enigma
from enigma_classes.plugboard_class import Plugboard
from enigma_classes.reflector_class import Reflector
from enigma_classes.rotor_class import Rotor


class ElementsDatabase():

    """Represents database of available rotors and
    reflectors for the machine"""

    def __init__(self, elements_data) -> None:
        rotors = {}
        reflectors = {}
        for rotor in elements_data["rotors"]:
            element = Rotor(rotor["name"], rotor["wiring"], rotor["indentation"])
            rotors[element.name] = element
        for reflector in elements_data["reflectors"]:
            element = Reflector(reflector["name"], reflector["wiring"])
            reflectors[element.name] = element
        self._rotors = rotors
        self._reflectors = reflectors

    def __add__(self, other):
        self._rotors = {**self.rotors, **other.rotors}
        self._reflectors = {**self.reflectors, **other.reflectors}
        return self

    @property
    def rotors(self):
        return self._rotors

    @property
    def reflectors(self):
        return self._reflectors

    def add_rotor(self, name, wiring, indentation):

        """Add new rotor model to custom json database"""

        new_element = Rotor(name, wiring, indentation)
        self.rotors.append(new_element)

    def add_reflector(self, name, wiring):

        """Add new reflector model to custom json database"""

        new_element = Reflector(name, wiring)
        self.reflectors.append(new_element)

    def remove_rotor(self, position):

        """Remove rotor model from custom json database"""

        self.rotors.pop(position)

    def remove_reflector(self, position):

        """Remove reflector model from custom json database"""

        self.reflectors.pop(position)

    def modify_reflector(self, positon, name, wiring):
        self.reflectors[positon].set_name(name)
        self.reflectors[positon].set_wiring(wiring)

    def modify_rotor(self, position, name, wiring, indentation):
        self.rotors[position].set_name(name)
        self.rotors[position].set_wiring(wiring)
        self.rotors[position].set_indentation(indentation)


class Configuration():
    def __init__(self, conf_data) -> None:
        self._rotors = conf_data["machine"]["rotors"]
        self._reflector = conf_data["machine"]["reflector"]
        self._positions = conf_data["machine"]["start_positions"]
        self._rings = conf_data["machine"]["rings"]
        self._plugboard = conf_data["machine"]["plugboard"]
        self._double_step = conf_data["settings"]["double_step"]
        self._space_dist = conf_data["settings"]["space_dist"]

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

    @property
    def double_step(self):
        return self._double_step

    @property
    def space_dist(self):
        return self._space_dist

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

    def initialize_enigma(self, database: ElementsDatabase):

        """Initialize an instance of enigma class
         with specified  configuration """

        rotors = [database.rotors[rotor] for rotor in self.rotors]
        reflector = database.reflectors[self.reflector]
        plugboard = Plugboard(self.plugboard)
        start_positions = self.positions
        rings = self.rings
        double_step = self.double_step
        enigma = Enigma(rotors, reflector, plugboard,
                        start_positions, rings, double_step)
        return enigma


class ResourcesManager():

    """Global manager - handling all resources json file"""

    def __init__(self, rsc_path) -> None:
        self.rsc_path = rsc_path
        self._default = self.get_default_database()
        self._custom = self.get_custom_database()
        self._conf = self.setup_config()
        self._elements = self.connect_data()
        print(self._elements.rotors)

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

    def setup_config(self, config_path=None) -> Configuration:
        if config_path is None:
            config_path = f"{self.rsc_path}/config.json"
        configuration = read_from_json(config_path)
        return Configuration(configuration)

    def set_config(self, configuration: Configuration):
        conf_data = {}
        conf_data["machine"]["rotors"] = configuration.rotors
        conf_data["machine"]["reflector"] = configuration.reflector
        conf_data["machine"]["start_positions"] = configuration.positions
        conf_data["machine"]["rings"] = configuration.rings
        conf_data["machine"]["plugboard"] = configuration.plugboard
        conf_data["settings"]["double_step"] = configuration.double_step
        conf_data["settings"]["space_dist"] = configuration.space_dist
        config_path = f"{self.rsc_path}/config.json"
        write_to_json(config_path, conf_data)
        self._conf = self.setup_config()

    def get_custom_database(self):
        custom_path = f"{self.rsc_path}/custom.json"
        return ElementsDatabase(read_from_json(custom_path))

    def get_default_database(self):
        default_path = f"{self.rsc_path}/default.json"
        return ElementsDatabase(read_from_json(default_path))

    def set_custom_database(self):
        data = {}
        data["rotors"] = [{"name": rotor.name,
                           "wiring": rotor.wiring,
                           "indentation": rotor.indentation}
                          for rotor in self.custom.rotors]
        data["reflectors"] = [{"name": reflector.name,
                               "wiring": reflector.wiring}
                              for reflector in self.custom.reflectors]
        custom_path = f"{self.rsc_path}/custom.json"
        write_to_json(custom_path, data)
        self._elements = self.connect_data()

    def connect_data(self):
        new_data = self.custom + self.default
        return new_data
