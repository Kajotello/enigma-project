from types import new_class
from enigma_classes.functions import str_change, swap, str_swap_down, to_letter
from enigma_gui.functions import read_from_json, str_to_plugboard, write_to_json, str_swap_up
from enigma_classes.enigma_class import Enigma
from enigma_classes.plugboard_class import Plugboard
from enigma_classes.reflector_class import Reflector
from enigma_classes.rotor_class import Rotor
from copy import deepcopy


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

        """Add new rotor model to custom json database"""

        new_element = Rotor(name, wiring, indentation)
        self.rotors[name] = new_element

    def add_reflector(self, name, wiring):

        """Add new reflector model to custom json database"""

        new_element = Reflector(name, wiring)
        self.reflectors[name] = new_element

    def remove_rotor(self, name):

        """Remove rotor model from custom json database"""

        self.rotors.pop(name)

    def remove_reflector(self, name):

        """Remove reflector model from custom json database"""

        self.reflectors.pop(name)

    def modify_reflector(self, old_name, name, wiring):
        wiring = str_to_plugboard(wiring)
        new_ref = Reflector(name, wiring)
        self.reflectors.pop(old_name)
        self.reflectors[name] = new_ref

    def modify_rotor(self, old_name, name, wiring, indentation):
        new_rotor = Rotor(name, wiring, indentation)
        self.rotors.pop(old_name)
        self.rotors[name] = new_rotor


class MachineConfiguration():
    def __init__(self, machine_conf) -> None:
        self._rotors = machine_conf["rotors"]
        self._reflector = machine_conf["reflector"]
        self._positions = machine_conf["start_positions"]
        self._rings = machine_conf["rings"]
        self._plugboard = machine_conf["plugboard"]

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
        self._rings = str_change(self.rings, index, new_ring)

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

    def update_positions(self, enigma: Enigma):
        position = ""
        for rotor in enigma.rotors:
            position += to_letter(rotor.position)
        self._positions = position


class Configuration():
    def __init__(self, conf_data) -> None:
        self._machine = MachineConfiguration(conf_data["machine"])
        self._double_step = conf_data["settings"]["double_step"]
        self._space_dist = conf_data["settings"]["space_dist"]

    @property
    def double_step(self):
        return self._double_step

    @property
    def space_dist(self):
        return self._space_dist

    @property
    def machine(self):
        return self._machine

    def change_machine_conf(self, new_machine_conf):
        self._machine = new_machine_conf

    def initialize_enigma(self, database: ElementsDatabase):

        """Initialize an instance of enigma class
         with specified  configuration """

        rotors = [deepcopy(database.rotors[rotor])
                  for rotor in self.machine.rotors]
        reflector = database.reflectors[self.machine.reflector]
        plugboard = Plugboard(self.machine.plugboard)
        start_positions = self.machine.positions
        rings = self.machine.rings
        double_step = self.double_step
        enigma = Enigma(rotors, reflector, plugboard,
                        start_positions, rings, double_step)
        return enigma

    def change_space_dist(self, new_space_dist):
        self._space_dist = new_space_dist


class ResourcesManager():

    """Global manager - handling all resources json file"""

    def __init__(self, rsc_path) -> None:
        self.rsc_path = rsc_path
        self._default = self.get_default_database()
        self._custom = self.get_custom_database()
        self._conf = self.setup_config()
        self._elements = self.connect_data()

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
        machine = {}
        settings = {}
        machine["rotors"] = configuration.machine.rotors
        machine["reflector"] = configuration.machine.reflector
        machine["start_positions"] = configuration.machine.positions
        machine["rings"] = configuration.machine.rings
        machine["plugboard"] = configuration.machine.plugboard
        settings["double_step"] = configuration.double_step
        settings["space_dist"] = configuration.space_dist

        conf_data["machine"] = machine
        conf_data["settings"] = settings

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
                          for rotor in self.custom.rotors.values()]
        data["reflectors"] = [{"name": reflector.name,
                               "wiring": reflector.wiring}
                              for reflector in self.custom.reflectors.values()]
        custom_path = f"{self.rsc_path}/custom.json"
        write_to_json(custom_path, data)
        self._elements = self.connect_data()

    def connect_data(self):
        new_data = self.custom + self.default
        return new_data
