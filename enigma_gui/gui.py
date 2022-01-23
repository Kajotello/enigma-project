
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow, QListWidgetItem
from enigma_classes.plugboard_class import PlugboardDuplicatedLetterError
from enigma_classes.plugboard_class import PlugboardInvalidFormatError
from enigma_classes.plugboard_class import PlugboardInvalidSignError
from enigma_classes.rotor_class import RotorIndentationDuplicatedLetterError
from enigma_classes.rotor_class import RotorIndentationInvalidSignError
from enigma_classes.rotor_class import RotorInvalidIndentationFormatError
from enigma_classes.rotor_class import RotorWiringInvalidSignEroor
from enigma_classes.rotor_class import RotorEmptyNameError
from enigma_classes.rotor_class import RotorWiringNotAllLettersError
from enigma_classes.rotor_class import RotorWiringDuplicatedLetterError
from enigma_classes.reflector_class import ReflectorEmptyNameError
from enigma_classes.reflector_class import ReflectorInvalidSignError
from enigma_classes.reflector_class import ReflectorNotAllLettersError
from enigma_classes.reflector_class import ReflectorDuplicatedLetterError
from enigma_classes.reflector_class import ReflectorInvalidWiringError
from enigma_classes.enigma_class import ReflectorNotInDatabaseError
from enigma_classes.enigma_class import RotorNotInDatabaseError
from enigma_classes.enigma_class import InvalidSignToCode
from enigma_gui.table_models import StepsTableModel, RotorsTableModel
from enigma_gui.main_window import Ui_MainWindow
from elements_database import NameInUseError, NotUniqueKeyError
from rsc_manager import ResourcesManager, InvalidConfJSONFileFormat
from rsc_manager import InvalidDatabaseJSONFileFormat, NotAJSONError
from functools import partial
import enigma_gui.dialogs as dialog
import enigma_gui.errors as error
import os


class EnigmaWindow(QMainWindow):
    def __init__(self, args, parent=None) -> None:
        super().__init__(parent)

        # get the current directory and set the path to resources directory
        cwd = os.getcwd()
        rsc_path = f"{cwd}/rsc"

        # define window properities
        self.selected_id = None
        self.ui = Ui_MainWindow()
        self.input = args.input_file
        self.output = args.output_file
        self.config = args.config
        self.rsc = ResourcesManager(rsc_path)
        self.enigma = self.rsc.initailze_enigma_with_file(
                args.config)
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # setup UI
        self.ui.setupUi(self)

        # connect change pages action
        self.ui.enc_by_letter_act.triggered.connect(partial(self.change_pg, 0))
        self.ui.en_from_file_act.triggered.connect(partial(self.change_pg, 1))
        self.ui.settings_act.triggered.connect(partial(self.change_pg, 2))
        self.ui.change_config_act.triggered.connect(partial(self.change_pg, 3))
        self.ui.a_r_rotor_act.triggered.connect(partial(self.change_pg, 4))
        self.ui.a_r_reflector_act.triggered.connect(partial(self.change_pg, 5))

        # connect signals by pages in stack

        #   page 0 - encrypt letter by letter
        #       buttons
        self.ui.encrypt_button.clicked.connect(self.encrypt_letter)

        #   page 1 - encrypt from file
        #       buttons
        self.ui.brow_input_butt.clicked.connect(partial(self.brow_file, "i"))
        self.ui.brow_output_butt.clicked.connect(partial(self.brow_file, "o"))
        self.ui.encrypt_file_button.clicked.connect(self.encrypt_file)

        #   page 2 - settings
        #       buttons
        self.ui.save_sett_def_butt.clicked.connect(self.save_def_sett)
        #       check boxes
        self.ui.is_double_step.stateChanged.connect(self.change_double_step)
        #       spin boxes
        self.ui.space_info.valueChanged.connect(self.change_space)

        #   page 3 - change configuration
        #       buttons
        self.ui.up_button.clicked.connect(self.rotor_swap_up)
        self.ui.down_button.clicked.connect(self.rotor_swap_down)
        self.ui.remove_button.clicked.connect(self.remove_rotor)
        self.ui.add_button.clicked.connect(self.add_rotor)
        self.ui.set_plugboard_button.clicked.connect(self.set_plugboard)
        self.ui.save_def_conf_button.clicked.connect(self.save_def_conf)
        self.ui.load_conf_button.clicked.connect(self.load_conf)
        self.ui.restore_conf_button.clicked.connect(self.restore_conf)
        self.ui.export_button.clicked.connect(self.export_conf)
        #       combo boxes
        self.ui.ring_comboBox.activated.connect(self.change_ring)
        self.ui.pos_comboBox.activated.connect(self.change_pos)
        self.ui.reflector_comboBox.activated.connect(self.change_reflector)
        #       line edit
        self.ui.plugboard_line.textChanged.connect(
            self.show_colored_alphabet_plugboard)

        #   page 4 - manage custom rotors
        #       buttons
        self.ui.mod_rotor_butt.clicked.connect(self.modify_rotor_model)
        self.ui.add_rotor_mod.clicked.connect(self.open_add_rotor_model)
        self.ui.add_mod_rotor.clicked.connect(self.add_rotor_model)
        self.ui.cancel_add_rotor.clicked.connect(self.cancel_add_rotor_model)
        self.ui.rem_rotor_mod.clicked.connect(self.remove_rotor_model)
        self.ui.add_from_file_rotor_button.clicked.connect(
            self.load_models_from_file)
        #   line edit
        self.ui.rotor_wiring.textChanged.connect(
            self.show_colored_alphabet_add_rotor)
        self.ui.rotor_wiring_2.textChanged.connect(
            self.show_colored_alphabet_mod_rotor)

        #   page 5 - manage custom reflectors
        #       buttons
        self.ui.modify_ref_button.clicked.connect(self.modify_ref)
        self.ui.add_ref_mod_butt.clicked.connect(self.open_add_ref_model)
        self.ui.add_mod_ref.clicked.connect(self.add_ref_model)
        self.ui.cancel_add_ref.clicked.connect(self.cancel_add_ref_model)
        self.ui.rem_ref_mod_button.clicked.connect(self.remove_ref_model)
        self.ui.add_from_file_ref_butt.clicked.connect(
            self.load_models_from_file)
        # line edit
        self.ui.reflector_mod_wiring.textChanged.connect(
            self.show_colored_alphabet_mod_ref)
        self.ui.reflector_mod_wiring_2.textChanged.connect(
            self.show_colored_alphabet_add_ref)

        # add alphabet letters to comboboxes which need that
        self.ui.pos_comboBox.addItems(self.alphabet)
        self.ui.ring_comboBox.addItems(self.alphabet)

        # load all dynamic widgets
        self.reload()

        # set "encrypt letter by letter" as starting page
        self.ui.stack.setCurrentIndex(0)

    def reload(self):

        """Reload dynamic widgets on all pages of EnigmaWindow"""

        # reset selected item
        self.selected_id = None

        # update database with available elements
        self.enigma.set_database(self.rsc.elements)

        plugboard_text = self.enigma.plugboard.connections
        # generate data about rotors in machine for display in table
        data = [[rotor.name, to_letter(rotor.position),
                to_letter(rotor.ring)] for rotor in self.enigma.rotors]

        # set dynamic widgets

        #   page 0 - encrypt letter by letter
        self.ui.current_config.setModel(RotorsTableModel(data))
        self.ui.reflector_name.setText(self.enigma.reflector.name)
        self.ui.plugboard_connections.setText(plugboard_text)

        #   page 1 - encrypt from file
        self.ui.input_file_name.setText(self.input)
        self.ui.output_file_name.setText(self.output)

        #   page 2 - settings
        self.ui.space_info.setValue(self.enigma.space_dist)
        if len(self.enigma.rotors) != 3:
            if self.ui.is_double_step.isChecked():
                self.ui.is_double_step.setChecked(False)
            self.ui.is_double_step.setEnabled(False)
        if len(self.enigma.rotors) == 3:
            self.ui.is_double_step.setEnabled(True)
            self.ui.is_double_step.setChecked(self.enigma.double_step)

        #   page 3 - change configuration
        self.ui.stack2.setCurrentIndex(0)
        self.setup_rotors()
        self.ui.reflector_comboBox.clear()
        self.ui.reflector_comboBox.addItems(self.rsc.elements.reflectors)
        self.ui.reflector_comboBox\
            .setCurrentText(self.enigma.reflector.name)
        self.ui.plugboard_line.setText(plugboard_text)

        #   page 4 - manage custom rotors
        self.ui.stack3.setCurrentIndex(0)
        self.setup_rotors_models()

        #   page 5 - manage custom reflectors
        self.ui.stack4.setCurrentIndex(0)
        self.setup_reflectors_models()

    #
    # Methods connected to widgets
    #

    #   page 0 - encrypt letter by letter
    def encrypt_letter(self):

        # read data and clear input line
        letter = self.ui.letter_input.text()
        self.ui.letter_input.clear()
        cipher_text = self.ui.cipher_text.text()

        try:

            # code letter and add it to cipher_text
            cipher_letter, steps_data = self.enigma.code_letter(letter)
            cipher_text += cipher_letter

            # reload dynamic widgets on page
            self.ui.steps_table\
                .setModel(StepsTableModel(self.generate_labels(), steps_data))
            self.ui.steps_table.horizontalHeader().hide()
            self.ui.cipher_text.setText(cipher_text)
            self.reload()
        except InvalidSignToCode:
            error.invalid_input()

    #   page 1 - encrypt from file
    def brow_file(self, type):

        filename = dialog.file_dialog(any_file=True)

        if filename:
            if type == "i":
                self.input = str(filename[0])
                self.ui.input_file_name.setText(str(filename[0]))
            elif type == "o":
                self.output = str(filename[0])
                self.ui.output_file_name.setText(str(filename[0]))

    def encrypt_file(self):
        try:
            self.enigma.code_file(self.input, self.output)
            dialog.compleated()
        except InvalidSignToCode:
            error.invalid_sign_in_file()
        except FileNotFoundError:
            error.not_file_with_name()
        except TypeError:
            # TypeErrror occurs when code button is pressed before choosen
            error.file_not_selected_yet()

    #   page 2 - settings
    def save_def_sett(self):
        self.rsc.save_new_default_config(self.enigma, "settings")
        dialog.default_setting_change()

    def change_double_step(self):
        if self.enigma.double_step is not self.ui.is_double_step.isChecked():
            self.enigma.change_double_step()

    def change_space(self):
        self.enigma.change_space_dist(self.ui.space_info.value())

    #   page 3 - change configuration
    def rotor_swap_up(self):
        if self.selected_id is None:
            return None
        self.enigma.move_rotor_up(self.selected_id)
        self.clear_rotors()
        self.setup_rotors()

        # probably it wil be good idea to connect it with display_rotors_info
        if self.selected_id != 0:
            self.ui.rotors_list.setCurrentRow(self.selected_id-1)
            self.selected_id -= 1
        else:
            self.ui.rotors_list.setCurrentRow(self.selected_id)

    def rotor_swap_down(self):
        if self.selected_id is None:
            return None
        self.enigma.move_rotor_down(self.selected_id)
        self.clear_rotors()
        self.setup_rotors()
        if self.selected_id != len(self.enigma.rotors)-1:
            self.ui.rotors_list.setCurrentRow(self.selected_id+1)
            self.selected_id += 1
        else:
            self.ui.rotors_list.setCurrentRow(self.selected_id)

    def remove_rotor(self):
        if self.selected_id is not None:
            self.enigma.remove_rotor(self.selected_id)
            self.selected_id = None
            self.ui.stack2.setCurrentIndex(0)
            self.clear_rotors()
            self.setup_rotors()

    def add_rotor(self):
        rotor_pos = dialog.add_rotor(self.rsc.elements)
        if rotor_pos == -1:
            return None
        rotor_name = list(self.rsc.elements.rotors.keys())[rotor_pos]
        self.enigma.add_rotor(rotor_name)
        self.clear_rotors()
        self.setup_rotors()

    def set_plugboard(self):
        plugboard = self.ui.plugboard_line.text()
        plugboard = plugboard.strip()

        try:
            self.enigma.set_plugboard(plugboard)
            self.ui.plugboard_line.setText(plugboard)
        except PlugboardInvalidFormatError:
            error.invalid_plugboard_format()
        except PlugboardInvalidSignError:
            error.invalid_sign()
        except PlugboardDuplicatedLetterError:
            error.duplciated_letter()

    def save_def_conf(self):
        self.rsc.save_new_default_config(self.enigma, 'machine')
        dialog.def_config_change()

    def load_conf(self):

        filename = dialog.file_dialog(['JSON file (*.json)'])

        if filename:
            try:
                self.enigma = self.rsc.initailze_enigma_with_file(filename[0])
            except InvalidConfJSONFileFormat:
                error.invalid_conf_JSON()
            except NotAJSONError:
                error.not_a_JSON()
            except RotorNotInDatabaseError:
                error.rotor_not_in_database()
            except ReflectorNotInDatabaseError:
                error.reflector_not_in_database()

        self.reload()

    def restore_conf(self):
        self.enigma = self.rsc.initialize_enigma()
        self.reload()

    def export_conf(self):

        filename = dialog.file_dialog(["JSON files (*.json)"], True)

        if filename:
            self.rsc.export_config_to_file(self.enigma, filename[0])

    def change_ring(self):
        new_ring = str(self.ui.ring_comboBox.currentText())
        self.enigma.change_ring(self.selected_id, new_ring)

    def change_pos(self):
        new_pos = str(self.ui.pos_comboBox.currentText())
        self.enigma.change_position(self.selected_id, new_pos)

    def change_reflector(self):
        new_reflector = str(self.ui.reflector_comboBox.currentText())
        self.enigma.change_reflector(new_reflector)

    def show_colored_alphabet_plugboard(self):
        text = self.ui.plugboard_line.text()
        result = self.generate_colored_alphabet(text)
        self.ui.alphabet_label.setText(result)

    #   page 4 - manage custom rotors
    def modify_rotor_model(self):
        name = self.ui.rotor_name_2.text()
        wiring = self.ui.rotor_wiring_2.text()
        indentations = self.ui.rotor_indentation_2.text()
        old_name = self.selected_id
        try:
            if (self.selected_id not in
                    [rotor.name for rotor in self.enigma.rotors] and
                    self.selected_id not in
                    self.rsc.conf['machine']['rotors']):
                self.rsc.custom.modify_rotor(
                    old_name, name, wiring, indentations)
                self.ui.stack3.setCurrentIndex(0)
                self.rsc.set_custom_database()
                self.setup_rotors_models()
                self.selected_id = None
            else:
                error.current_use_error()
        except NameInUseError:
            error.name_in_use()
        except RotorWiringInvalidSignEroor:
            error.invalid_sign()
        except RotorWiringDuplicatedLetterError:
            error.duplciated_letter()
        except RotorEmptyNameError:
            error.empty_name()
        except RotorWiringNotAllLettersError:
            error.invalid_rotor_wiring()
        except RotorIndentationDuplicatedLetterError:
            error.indentations_duplicated_letter()
        except RotorIndentationInvalidSignError:
            error.indentations_invalid_sign()
        except RotorInvalidIndentationFormatError:
            error.indenations_invalid_format()

    def open_add_rotor_model(self):
        self.ui.rotor_wiring.setText("A")
        self.ui.rotor_wiring.setText("")
        self.ui.stack3.setCurrentIndex(2)

    def add_rotor_model(self):
        name = self.ui.rotor_name.text()
        wiring = self.ui.rotor_wiring.text()
        indentations = self.ui.rotor_indentation.text()
        try:
            self.rsc.custom.add_rotor(name, wiring, indentations)
            self.rsc.set_custom_database()
            self.ui.stack3.setCurrentIndex(0)
            self.setup_rotors_models()
            self.ui.rotor_name.clear()
            self.ui.rotor_wiring.clear()
            self.ui.rotor_indentation.clear()
        except NameInUseError:
            error.name_in_use()
        except RotorWiringInvalidSignEroor:
            error.invalid_sign()
        except RotorWiringDuplicatedLetterError:
            error.duplciated_letter()
        except RotorEmptyNameError:
            error.empty_name()
        except RotorWiringNotAllLettersError:
            error.invalid_rotor_wiring()
        except RotorIndentationDuplicatedLetterError:
            error.indentations_duplicated_letter()
        except RotorIndentationInvalidSignError:
            error.indentations_invalid_sign()
        except RotorInvalidIndentationFormatError:
            error.indenations_invalid_format()

    def cancel_add_rotor_model(self):
        self.ui.stack3.setCurrentIndex(0)
        self.ui.rotor_name.clear()
        self.ui.rotor_wiring.clear()
        self.ui.rotor_indentation.clear()

    def remove_rotor_model(self):
        if self.selected_id is None:
            pass
        elif (self.selected_id not in
              [rotor.name for rotor in self.enigma.rotors] and
              self.selected_id not in self.rsc.
                conf['machine']['rotors']):
            self.rsc.custom.remove_rotor(self.selected_id)
            self.rsc.set_custom_database()
            self.setup_rotors_models()
            self.ui.stack3.setCurrentIndex(0)
            self.selected_id = None
        else:
            error.current_use_error()

    def show_colored_alphabet_add_rotor(self):
        text = self.ui.rotor_wiring.text()
        result = self.generate_colored_alphabet(text)
        self.ui.alphabet_label_2.setText(result)

    def show_colored_alphabet_mod_rotor(self):
        text = self.ui.rotor_wiring_2.text()
        result = self.generate_colored_alphabet(text)
        self.ui.alphabet_label_3.setText(result)

    def load_models_from_file(self):

        filename = dialog.file_dialog(["JSON files (*.json)"])

        if filename:
            try:
                self.rsc.add_new_elements_from_file(filename[0])
                self.ui.stack3.setCurrentIndex(0)
                self.setup_rotors_models()
                self.ui.rotor_name.clear()
                self.ui.rotor_wiring.clear()
                self.ui.rotor_indentation.clear()
                self.ui.stack4.setCurrentIndex(0)
                self.rsc.set_custom_database()
                self.setup_reflectors_models()
            except InvalidDatabaseJSONFileFormat:
                error.invalid_db_JSON()
            except NotAJSONError:
                error.not_a_JSON()
            except NotUniqueKeyError:
                error.failed_elements_load_duplicated_name()
            except NameInUseError:
                error.failed_elements_load_duplicated_name()

    #   page 5 - manage custom reflectors
    def modify_ref(self):
        name = self.ui.reflector_mod_name.text()
        wiring = self.ui.reflector_mod_wiring.text()
        old_name = self.selected_id
        try:
            if (self.selected_id != self.enigma.reflector.name and
                    self.selected_id != self.rsc.conf['machine']['reflector']):
                self.rsc.custom.modify_reflector(old_name, name, wiring)
                self.ui.stack4.setCurrentIndex(0)
                self.rsc.set_custom_database()
                self.setup_reflectors_models()
                self.selected_id = None
            else:
                error.current_use_error()
        except NameInUseError:
            error.name_in_use()
        except ReflectorInvalidWiringError:
            error.invalid_reflector_wiring()
        except ReflectorInvalidSignError:
            error.invalid_sign()
        except ReflectorEmptyNameError:
            error.empty_name()
        except ReflectorDuplicatedLetterError:
            error.duplciated_letter()
        except ReflectorNotAllLettersError:
            error.invalid_reflector_wiring()

    def open_add_ref_model(self):
        self.ui.reflector_mod_wiring_2.setText("A")
        self.ui.reflector_mod_wiring_2.setText("")
        self.ui.stack4.setCurrentIndex(2)

    def add_ref_model(self):
        name = self.ui.reflector_mod_name_2.text()
        wiring = self.ui.reflector_mod_wiring_2.text()
        try:
            self.rsc.custom.add_reflector(name, wiring)
            self.ui.stack4.setCurrentIndex(0)
            self.rsc.set_custom_database()
            self.setup_reflectors_models()
            self.ui.reflector_mod_name_2.clear()
            self.ui.reflector_mod_wiring_2.clear()
        except NameInUseError:
            error.name_in_use()
        except ReflectorInvalidWiringError:
            error.invalid_reflector_wiring()
        except ReflectorInvalidSignError:
            error.invalid_sign()
        except ReflectorEmptyNameError:
            error.empty_name()
        except ReflectorDuplicatedLetterError:
            error.duplciated_letter()
        except ReflectorNotAllLettersError:
            error.invalid_reflector_wiring()

    def cancel_add_ref_model(self):
        self.ui.stack4.setCurrentIndex(0)
        self.ui.reflector_mod_name_2.clear()
        self.ui.reflector_mod_wiring_2.clear()

    def remove_ref_model(self):
        if self.selected_id is None:
            pass
        elif (self.selected_id != self.enigma.reflector.name and
              self.selected_id != self.rsc.
              conf['machine']['reflector']):
            self.rsc.custom.remove_reflector(self.selected_id)
            self.setup_reflectors_models()
            self.rsc.set_custom_database()
            self.ui.stack4.setCurrentIndex(0)
            self.ui.reflector_mod_name.clear()
            self.ui.reflector_mod_wiring.clear()
            self.selected_id = None
        else:
            error.current_use_error()

    def show_colored_alphabet_add_ref(self):
        text = self.ui.reflector_mod_wiring_2.text()
        result = self.generate_colored_alphabet(text)
        self.ui.alphabet_label_5.setText(result)

    def show_colored_alphabet_mod_ref(self):
        text = self.ui.reflector_mod_wiring.text()
        result = self.generate_colored_alphabet(text)
        self.ui.alphabet_label_4.setText(result)

    # setups and click handler for lists widgets
    # page 0
    def setup_rotors(self):
        self.ui.rotors_list.clear()
        rotors = self.enigma.rotors
        for i, rotor in enumerate(rotors):
            item = QListWidgetItem(rotor.name)
            self.ui.rotors_list.addItem(item)
            item.position = i
        self.ui.rotors_list.itemClicked.connect(self.display_rotor_info)

    def display_rotor_info(self, item):
        self.selected_id = int(item.position)
        self.ui.stack2.setCurrentIndex(1)
        self.ui.ring_comboBox.setCurrentIndex(
            self.enigma.rotors[self.selected_id].ring)
        self.ui.pos_comboBox.setCurrentIndex(
            self.enigma.rotors[self.selected_id].position)

    def clear_rotors(self):
        self.ui.rotors_list.clear()

    # page 4
    def setup_rotors_models(self):
        self.ui.rotors_list_2.clear()
        rotors = self.rsc.custom.rotors
        for i, rotor in enumerate(rotors):
            item = QListWidgetItem(rotor)
            self.ui.rotors_list_2.addItem(item)
            item.position = i
        self.ui.rotors_list_2.itemClicked.connect(
            self.display_rotor_model_info)

    def display_rotor_model_info(self, item):
        self.selected_id = item.text()
        self.ui.stack3.setCurrentIndex(1)
        self.ui.rotor_name_2.setText(item.text())
        self.ui.rotor_wiring_2.setText(
            self.rsc.custom.rotors[self.selected_id].wiring)
        self.ui.rotor_indentation_2.setText(
            self.rsc.custom.rotors[self.selected_id].indentations_str)

    # page 5
    def setup_reflectors_models(self):
        self.ui.reflectors_list.clear()
        reflectors = self.rsc.custom.reflectors
        for i, reflector in enumerate(reflectors):
            item = QListWidgetItem(reflector)
            self.ui.reflectors_list.addItem(item)
            item.position = i
        self.ui.reflectors_list.itemClicked.connect(
            self.display_reflector_model_info)

    def display_reflector_model_info(self, item):
        self.selected_id = item.text()
        self.ui.stack4.setCurrentIndex(1)
        self.ui.reflector_mod_name.setText(item.text())
        self.ui.reflector_mod_wiring.setText(
            self.rsc.custom.reflectors[self.selected_id].wiring)

    def change_pg(self, page_number):
        self.reload()
        self.set_page(page_number)

    # Other methods
    def set_page(self, index):
        self.ui.stack.setCurrentIndex(index)

    def generate_labels(self):
        label = ["Input", "Plugboard Encryption"]
        for i in range(len(self.enigma.rotors)):
            label.append(f"{len(self.enigma.rotors)-i}. Rotor Encryption")
        label.append("Reflector Encryption")
        for i in range(len(self.enigma.rotors)):
            label.append(f"{i+1}. Rotor Encryption")
        label.append("Plugboard Encryption")
        label.append("Output")
        return label

    def generate_colored_alphabet(self, text):

        """Generate colored alphabet for given text:
        - green color if letter is not in text
        - black color if letter is in the text once
        - red color if letter is in the text more than once"""

        result = ""
        open_tag_green = '<span style=" font-weight:600; color:#32b51e;">'
        open_tag_black = '<span style=" font-weight:600; color:#000000;">'
        open_tag_red = '<span style=" font-weight:600; color:#d02222;">'
        close_tag = '</span> '
        for letter in self.alphabet:
            if text.count(letter) == 0:
                result += f'{open_tag_green}{letter}{close_tag} '
            elif text.count(letter) == 1:
                result += f'{open_tag_black}{letter}{close_tag} '
            else:
                result += f'{open_tag_red}{letter}{close_tag} '

        return result


def to_letter(int: int) -> str:
    return chr(int+65)


def gui_main(args):
    app = QApplication()
    window = EnigmaWindow(args)
    window.show()
    return app.exec_()
