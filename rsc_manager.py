from enigma_classes.functions import to_letter
import json
from enigma_classes.enigma_class import Enigma, InvalidConfData
from elements_database import ElementsDatabase, CustomElementsDatabase
from elements_database import InvalidElementsDataError


class ResourcesManager():

    """Global manager - handling all resources json file"""

    def __init__(self, rsc_path) -> None:

        # path to resources files
        self.rsc_path = rsc_path
        custom_path = f"{self.rsc_path}/custom.json"
        default_path = f"{self.rsc_path}/default.json"
        config_path = f"{self.rsc_path}/config.json"

        # load databases from resources files
        try:
            self._default = ElementsDatabase(read_from_json(default_path))
        except InvalidElementsDataError:
            raise InvalidDatabaseJSONFileFormat('Default database file (./res/default.json) \
                have an invalid format')

        try:
            self._custom = CustomElementsDatabase(
                self._default, read_from_json(custom_path))
        except InvalidElementsDataError:
            raise InvalidDatabaseJSONFileFormat('Custom database file (./res/custom.json) \
                have an invalid format')

        self._elements = self.default + self.custom
        self._conf = read_from_json(config_path)

    @property
    def default(self):

        """Default elements database with no ability
         of modification"""

        return self._default

    @property
    def custom(self):

        """Custom elements database with full ability
        of modification"""

        return self._custom

    @property
    def conf(self):

        """Configuration dictionary read from config file"""

        return self._conf

    @property
    def elements(self):

        """Combined database of all available elements"""

        return self._elements

    def initialize_enigma(self) -> Enigma:

        """Initialize Enigma with configuration from config file"""

        try:
            return Enigma(self.conf, self.elements)
        except InvalidConfData:
            raise InvalidConfJSONFileFormat

    def initailze_enigma_with_file(self, path):

        """Initialize Enigma with configuration
        from another file given as an argument"""

        try:
            configuration = read_from_json(path)
            return Enigma(configuration, self.elements)

        except InvalidConfData:
            raise InvalidConfJSONFileFormat

    def export_config_to_file(self, enigma_machine, path):

        """Save current configuration of the machine (with settings)
        to file given as an argument"""

        conf_data = self.get_conf_from_enigma(enigma_machine)
        write_to_json(path, conf_data)

    def save_new_default_config(self, enigma_machine: Enigma, type):

        """Save current Enigma configuration to config file"""

        # if type is settings, manager will change
        # only properties in settings dictionary to match actual
        if type == 'settings':
            conf_data = self.get_settings_from_enigma(enigma_machine)

        # if type is machine, manager will change
        # only properties in machine dictionary to match actual
        elif type == 'machine':
            conf_data = self.get_conf_from_enigma(enigma_machine)

        # write data to config.json file
        config_path = f"{self.rsc_path}/config.json"
        write_to_json(config_path, conf_data)

        # actualize conf property to actual content of config.json file
        self._conf = conf_data

    def get_settings_from_enigma(self, enigma_machine: Enigma) -> dict:

        conf_data = self.conf
        settings = {}

        settings["double_step"] = enigma_machine.double_step
        settings["space_dist"] = enigma_machine.space_dist
        conf_data['settings'] = settings

        return conf_data

    def get_conf_from_enigma(self, enigma_machine: Enigma) -> dict:

        conf_data = self.conf
        machine = {}

        machine["rotors"] = []
        machine["rings"] = ""
        machine["start_positions"] = ""

        for rotor in enigma_machine.rotors:
            machine["rotors"].append(rotor.name)
            machine["rings"] += to_letter(rotor.ring)
            machine["start_positions"] += to_letter(rotor.position)

        machine["reflector"] = enigma_machine.reflector.name
        machine["plugboard"] = enigma_machine.plugboard.connections

        conf_data["machine"] = machine

        return conf_data

    def set_custom_database(self):

        """Write custom database content to custom.json"""

        data = {}

        # change data to proper format
        data["rotors"] = [{
                            "name": rotor.name,
                            "wiring": rotor.wiring,
                            "indentations": rotor.indentations_str,
                        } for rotor in self.custom.rotors.values()]
        data["reflectors"] = [{"name": reflector.name,
                               "wiring": reflector.wiring}
                              for reflector in self.custom.reflectors.values()]

        # write to custom.json file
        custom_path = f"{self.rsc_path}/custom.json"
        write_to_json(custom_path, data)

        # actualize elements property becuse
        # custom database has already changed
        self._elements = self.custom + self.default

    def add_new_elements_from_file(self, path):

        """Add new elements to custom database"""

        try:
            new_custom = CustomElementsDatabase(
                self.default, read_from_json(path))
            self._custom = new_custom + self.custom
            self.set_custom_database()
        except InvalidElementsDataError:
            raise InvalidDatabaseJSONFileFormat
        except Exception:
            raise


def read_from_json(path: str):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        raise NotAJSONError


def write_to_json(path: str, data) -> None:
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


class InvalidConfJSONFileFormat(Exception):
    pass


class InvalidDatabaseJSONFileFormat(Exception):
    pass


class NotAJSONError(Exception):
    pass
