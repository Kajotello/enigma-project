from PySide2.QtWidgets import QApplication, QFileDialog, QDialog
from PySide2.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from enigma_gui.dialog_windows import CustomDialog
from enigma_gui.table_models import StepsTableModel, RotorsTableModel
from enigma_gui.main_window import Ui_MainWindow
from rsc_manager import ResourcesManager
from copy import deepcopy
import os
from functools import partial
from enigma_gui.error_msgs import show_empty_name, show_invalid_sign_error
from enigma_gui.error_msgs import show_duplciated_letter_error
from enigma_gui.error_msgs import show_invalid_name
from enigma_gui.error_msgs import show_invalid_input_error
from enigma_gui.error_msgs import show_invalid_plugboard_format
from enigma_gui.error_msgs import show_invalid_rotor_wiring
from enigma_gui.error_msgs import show_invalid_reflector_wiring
from enigma_gui.error_msgs import show_current_use_error
from enigma_gui.validators import validate_plugboard, validate_new_rotor
from enigma_gui.validators import validate_input, validate_new_reflector

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


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
        self.enigma = self.rsc.conf

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
        self.ui.brow_config_butt.clicked.connect(partial(self.brow_file, "c"))
        self.ui.encrypt_file_button.clicked.connect(self.encrypt_file)

        #   page 2 - settings
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
        self.ui.save_conf_button.clicked.connect(self.save_conf)
        self.ui.save_init_conf_button.clicked.connect(self.save_init_conf)
        #       combo boxes
        self.ui.ring_comboBox.activated.connect(self.change_ring)
        self.ui.pos_comboBox.activated.connect(self.change_pos)
        self.ui.reflector_comboBox.activated.connect(self.change_reflector)
        #       line edit
        self.ui.plugboard_line.textChanged.connect(self.show_colored_alphabet_plugboard)

        #   page 4 - manage custom rotors
        #       buttons
        self.ui.mod_rotor_butt.clicked.connect(self.modify_rotor_model)
        self.ui.add_rotor_mod.clicked.connect(self.add_rotor_model)
        self.ui.add_mod_rotor.clicked.connect(self.add_this_rotor_model)
        self.ui.cancel_add_rotor.clicked.connect(self.cancel_rotor_add)
        self.ui.rem_rotor_mod.clicked.connect(self.remove_rotor_model)
        #   line edit
        self.ui.rotor_wiring.textChanged.connect(self.show_colored_alphabet_new_rotor)
        self.ui.rotor_wiring_2.textChanged.connect(self.show_colored_alphabet_mod_rotor)

        #   page 5 - manage custom reflectors
        #       buttons
        self.ui.modify_ref_button.clicked.connect(self.modify_reflector)
        self.ui.add_ref_mod_butt.clicked.connect(self.add_ref_model)
        self.ui.add_mod_ref.clicked.connect(self.add_mod_ref)
        self.ui.cancel_add_ref.clicked.connect(self.cancel_ref_add)
        self.ui.rem_ref_mod_button.clicked.connect(self.rem_mod_ref)
        # line edit
        self.ui.reflector_mod_wiring.textChanged.connect(self.show_colored_alphabet_mod_ref)
        self.ui.reflector_mod_wiring_2.textChanged.connect(self.show_colored_alphabet_add_ref)

        # add alphabet letters to comboboxes which need that
        self.ui.pos_comboBox.addItems(alphabet)
        self.ui.ring_comboBox.addItems(alphabet)

        # load all dynamic widgets
        self.reload()

        # set "encrypt letter by letter" as starting page
        self.ui.stack.setCurrentIndex(0)

    def reload(self):

        """Reload dynamic widgets on all pages of EnigmaWindow"""

        # reset selected item
        self.selected_id = None

        # update database with available elements
        self.enigma.update_database(self.rsc.elements)

        # remove existing change in temporary configuration
        self.temp = deepcopy(self.enigma)

        plugboard_text = self.enigma.plugboard.connections_str
        # generate data about rotors in machine for display in table
        data = [[rotor.name, to_letter(rotor.position),
                to_letter(rotor.ring)] for rotor in self.enigma.rotors]

        # set dynamic widgets

        #   page 0 - encrypt letter by letter
        self.ui.current_config.setModel(RotorsTableModel(data))
        self.ui.reflector_name.setText(self.enigma.reflector.name)
        self.ui.plugboard_connections.setText(plugboard_text)

        #   page 1 - encrypt from file
        self.ui.output_file_name.setText(self.output)
        self.ui.config_file_name.setText(self.config)

        #   page 2 - settings
        self.ui.space_info.setValue(self.enigma.space_dist)
        if len(self.enigma.rotors) != 3:
            if self.ui.is_double_step.isChecked():
                self.change_double_step()
            self.ui.is_double_step.setEnabled(False)
        if len(self.enigma.rotors) == 3:
            self.ui.is_double_step.setEnabled(True)

        #   page 3 - change configuration
        self.ui.stack2.setCurrentIndex(0)
        self.setupRotors()
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

        validation = validate_input(letter)

        if validation == 0:

            # code letter and add it to cipher_text
            cipher_letter, steps_data = self.enigma.code_letter(letter)
            cipher_text += cipher_letter

            # reload dynamic widgets on page
            self.ui.steps_table\
                .setModel(StepsTableModel(self.generate_labels(), steps_data))
            self.ui.steps_table.horizontalHeader().hide()
            self.ui.cipher_text.setText(cipher_text)
            self.reload()
        else:
            show_invalid_input_error()

    #   page 1 - encrypt from file
    def brow_file(self, type):

        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setViewMode(QFileDialog.Detail)

        if dialog.exec_() == QDialog.Accepted:
            filename = dialog.selectedFiles()

        if filename:
            if type == "i":
                self.input = str(filename[0])
                self.ui.input_file_name.setText(str(filename[0]))
            elif type == "o":
                self.output = str(filename[0])
                self.ui.output_file_name.setText(str(filename[0]))
            else:
                self.config = str(filename[0])
                self.ui.config_file_name.setText(str(filename[0]))

    def encrypt_file(self):

        file_encrypt_conf = self.rsc.get_config(self.config)
        file_encrypt_conf.code_file(self.input, self.output)
        show_compleated_dialog()

    #   page 2 - settings
    def change_double_step(self):
        if self.enigma.double_step is False:
            self.enigma.change_double_step()
        else:
            self.enigma.change_double_step()
            self.ui.is_double_step.setChecked(0)

    def change_space(self):
        self.enigma.change_space_dist(self.ui.space_info.value())

    #   page 3 - change configuration
    def rotor_swap_up(self):
        if self.selected_id is None:
            return None
        self.temp.move_rotor_up(self.selected_id)
        self.clear_rotors()
        self.setupRotors()

        # probably it wil be good idea to connect it with display_rotors_info
        if self.selected_id != 0:
            self.ui.rotors_list.setCurrentRow(self.selected_id-1)
            self.selected_id -= 1
        else:
            self.ui.rotors_list.setCurrentRow(self.selected_id)

    def rotor_swap_down(self):
        if self.selected_id is None:
            return None
        self.temp.move_rotor_down(self.selected_id)
        self.clear_rotors()
        self.setupRotors()
        if self.selected_id != len(self.temp.rotors)-1:
            self.ui.rotors_list.setCurrentRow(self.selected_id+1)
            self.selected_id += 1
        else:
            self.ui.rotors_list.setCurrentRow(self.selected_id)

    def remove_rotor(self):
        self.temp.remove_rotor(self.selected_id)
        self.selected_id = None
        self.ui.stack2.setCurrentIndex(0)
        self.clear_rotors()
        self.setupRotors()

    def add_rotor(self):
        rotor_pos = show_add_rotor_dialog(self.rsc.elements)
        if rotor_pos == -1:
            return None
        rotor_name = list(self.rsc.elements.rotors.keys())[rotor_pos]
        self.temp.add_rotor(rotor_name)
        self.clear_rotors()
        self.setupRotors()

    def set_plugboard(self):
        plugboard = self.ui.plugboard_line.text()
        plugboard = plugboard.strip()
        validation, error_sign = validate_plugboard(plugboard)
        if validation == 0:
            self.temp.set_plugboard(plugboard)
            self.ui.plugboard_line.setText(plugboard)
        elif validation == 1:
            show_invalid_plugboard_format()
        elif validation == 2:
            show_invalid_sign_error(error_sign)
        elif validation == 3:
            show_invalid_plugboard_format()
        elif validation == 4:
            show_duplciated_letter_error(error_sign)

    def save_conf(self):
        self.enigma = deepcopy(self.temp)
        show_config_change_dialog()

    def save_init_conf(self):
        self.rsc.set_config(self.temp)
        show_init_config_change_dialog()

    def change_ring(self):
        new_ring = str(self.ui.ring_comboBox.currentText())
        self.temp.change_ring(self.selected_id, new_ring)

    def change_pos(self):
        new_pos = str(self.ui.pos_comboBox.currentText())
        self.temp.change_position(self.selected_id, new_pos)

    def change_reflector(self):
        new_reflector = str(self.ui.reflector_comboBox.currentText())
        self.temp.change_reflector(new_reflector)

    def show_colored_alphabet_plugboard(self):
        text = self.ui.plugboard_line.text()
        result = generate_colored_alphabet(text)
        self.ui.alphabet_label.setText(result)

    #   page 4 - manage custom rotors
    def modify_rotor_model(self):
        name = self.ui.rotor_name_2.text()
        wiring = self.ui.rotor_wiring_2.text()
        indentation = self.ui.rotor_indentation_2.text()
        old_name = self.selected_id
        validation, error_sign = validate_new_rotor(wiring, name, self.rsc.elements, old_name)
        if validation == 0:
            self.rsc.custom.modify_rotor(old_name, name, wiring, indentation)
            # TO CHANGE IN THE FUTURE
            self.ui.stack3.setCurrentIndex(0)
            self.rsc.set_custom_database()
            self.setup_rotors_models()
        elif validation == 1:
            show_invalid_rotor_wiring()
        elif validation == 2:
            show_invalid_sign_error(error_sign)
        elif validation == 3:
            show_duplciated_letter_error(error_sign)
        elif validation == 4:
            show_invalid_name()
        elif validation == 5:
            show_empty_name()

    def add_rotor_model(self):
        self.ui.rotor_wiring.setText("A")
        self.ui.rotor_wiring.setText("")
        self.ui.stack3.setCurrentIndex(2)

    def add_this_rotor_model(self):
        name = self.ui.rotor_name.text()
        wiring = self.ui.rotor_wiring.text()
        indentation = self.ui.rotor_indentation.text()
        validation, error_sign = validate_new_rotor(wiring, name, self.rsc.elements)
        if validation == 0:
            self.rsc.custom.add_rotor(name, wiring, indentation)
            self.rsc.set_custom_database()
            self.ui.stack3.setCurrentIndex(0)
            self.setup_rotors_models()
            self.ui.rotor_name.clear()
            self.ui.rotor_wiring.clear()
            self.ui.rotor_indentation.clear()
        elif validation == 1:
            show_invalid_rotor_wiring()
        elif validation == 2:
            show_invalid_sign_error(error_sign)
        elif validation == 3:
            show_duplciated_letter_error(error_sign)
        elif validation == 4:
            show_invalid_name()
        elif validation == 5:
            show_empty_name()

    def cancel_rotor_add(self):
        self.ui.stack3.setCurrentIndex(0)
        self.ui.rotor_name.clear()
        self.ui.rotor_wiring.clear()
        self.ui.rotor_indentation.clear()

    def remove_rotor_model(self):
        if self.selected_id is None:
            pass
        elif (self.selected_id not in self.enigma.rotors and
              self.selected_id not in self.rsc.conf.rotors):
            self.rsc.custom.remove_rotor(self.selected_id)
            self.rsc.set_custom_database()
            self.setup_rotors_models()
            self.ui.stack3.setCurrentIndex(0)
        else:
            show_current_use_error()

    def show_colored_alphabet_new_rotor(self):
        text = self.ui.rotor_wiring.text()
        result = generate_colored_alphabet(text)
        self.ui.alphabet_label_2.setText(result)

    def show_colored_alphabet_mod_rotor(self):
        text = self.ui.rotor_wiring_2.text()
        result = generate_colored_alphabet(text)
        self.ui.alphabet_label_3.setText(result)

    #   page 5 - manage custom reflectors
    def modify_reflector(self):
        name = self.ui.reflector_mod_name.text()
        wiring = self.ui.reflector_mod_wiring.text()
        old_name = self.selected_id
        validation, error_sign = validate_new_reflector(wiring, name, self.rsc.elements, old_name)
        if validation == 0:
            self.rsc.custom.modify_reflector(old_name, name, wiring)
            self.ui.stack4.setCurrentIndex(0)
            self.rsc.set_custom_database()
            self.setup_reflectors_models()
            # to change
        elif validation == 1:
            show_invalid_reflector_wiring()
        elif validation == 2:
            show_invalid_reflector_wiring()
        elif validation == 3:
            show_invalid_sign_error(error_sign)
        elif validation == 4:
            show_invalid_reflector_wiring()
        elif validation == 5:
            show_invalid_reflector_wiring()
        elif validation == 6:
            show_invalid_name()
        elif validation == 7:
            show_empty_name()

    def add_ref_model(self):
        self.ui.reflector_mod_wiring_2.setText("A")
        self.ui.reflector_mod_wiring_2.setText("")
        self.ui.stack4.setCurrentIndex(2)

    def add_mod_ref(self):
        name = self.ui.reflector_mod_name_2.text()
        wiring = self.ui.reflector_mod_wiring_2.text()
        validation, error_sign = validate_new_reflector(wiring, name, self.rsc.elements)

        if validation == 0:
            self.rsc.custom.add_reflector(name, wiring)
            self.ui.stack4.setCurrentIndex(0)
            self.rsc.set_custom_database()
            self.setup_reflectors_models()
            self.ui.reflector_mod_name_2.clear()
            self.ui.reflector_mod_wiring_2.clear()
        elif validation == 1:
            show_invalid_reflector_wiring()
        elif validation == 2:
            show_invalid_reflector_wiring()
        elif validation == 3:
            show_invalid_sign_error(error_sign)
        elif validation == 4:
            show_invalid_reflector_wiring()
        elif validation == 5:
            show_invalid_reflector_wiring()
        elif validation == 6:
            show_invalid_name()
        elif validation == 7:
            show_empty_name()

    def cancel_ref_add(self):
        self.ui.stack4.setCurrentIndex(0)
        self.ui.reflector_mod_name_2.clear()
        self.ui.reflector_mod_wiring_2.clear()

    def rem_mod_ref(self):
        if self.selected_id is None:
            pass
        elif (self.selected_id != self.enigma.reflector and
              self.selected_id != self.rsc.conf.reflector):
            self.rsc.custom.remove_reflector(self.selected_id)
            self.setup_reflectors_models()
            self.rsc.set_custom_database()
            self.ui.stack4.setCurrentIndex(0)
            self.ui.reflector_mod_name.clear()
            self.ui.reflector_mod_wiring.clear()
        else:
            show_current_use_error()

    def show_colored_alphabet_add_ref(self):
        text = self.ui.reflector_mod_wiring_2.text()
        result = generate_colored_alphabet(text)
        self.ui.alphabet_label_5.setText(result)

    def show_colored_alphabet_mod_ref(self):
        text = self.ui.reflector_mod_wiring.text()
        result = generate_colored_alphabet(text)
        self.ui.alphabet_label_4.setText(result)

    def setup_rotors_models(self):
        self.ui.rotors_list_2.clear()
        rotors = self.rsc.custom.rotors
        for i, rotor in enumerate(rotors):
            item = QListWidgetItem(rotor)
            self.ui.rotors_list_2.addItem(item)
            item.position = i
        self.ui.rotors_list_2.itemClicked.connect(self.display_rotor_model_info)

    def display_rotor_model_info(self, item):
        self.selected_id = item.text()
        self.ui.stack3.setCurrentIndex(1)
        self.ui.rotor_name_2.setText(item.text())
        self.ui.rotor_wiring_2.setText(self.rsc.custom.rotors[self.selected_id].wiring)
        self.ui.rotor_indentation_2.setText(to_letter(self.rsc.custom.rotors[self.selected_id].indentation))

    def setup_reflectors_models(self):
        self.ui.reflectors_list.clear()
        reflectors = self.rsc.custom.reflectors
        for i, reflector in enumerate(reflectors):
            item = QListWidgetItem(reflector)
            self.ui.reflectors_list.addItem(item)
            item.position = i
        self.ui.reflectors_list.itemClicked.connect(self.display_reflector_model_info)

    def display_reflector_model_info(self, item):
        self.selected_id = item.text()
        self.ui.stack4.setCurrentIndex(1)
        self.ui.reflector_mod_name.setText(item.text())
        self.ui.reflector_mod_wiring.setText(self.rsc.custom.reflectors[self.selected_id].wiring)

    def change_pg(self, page_number):
        self.reload()
        self.set_page(page_number)

    def clear_rotors(self):
        self.ui.rotors_list.clear()

    def setupRotors(self):
        self.ui.rotors_list.clear()
        rotors = self.temp.rotors
        for i, rotor in enumerate(rotors):
            item = QListWidgetItem(rotor.name)
            self.ui.rotors_list.addItem(item)
            item.position = i
        self.ui.rotors_list.itemClicked.connect(self.display_rotor_info)

    def display_rotor_info(self, item):
        self.selected_id = int(item.position)
        self.ui.stack2.setCurrentIndex(1)
        self.ui.ring_comboBox.setCurrentIndex(self.temp.rotors[self.selected_id].ring)
        self.ui.pos_comboBox.setCurrentIndex(self.temp.rotors[self.selected_id].position)

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


def show_compleated_dialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Your encryption has been successfully ended.")
    msg.setWindowTitle("Encyryption compleated")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_init_config_change_dialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Your initial configuration has been changed.")
    msg.setWindowTitle("Initial configuration changed")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_config_change_dialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Your current configuration has been changed.")
    msg.setWindowTitle("Configuration changed")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_add_rotor_dialog(data):
    msg = CustomDialog(data)
    msg.setWindowTitle("Add rotor")

    return msg.exec_()


def generate_colored_alphabet(text):
    result = ""
    for letter in alphabet:
        if text.count(letter) == 0:
            result += f'<span style=" font-weight:600; color:#32b51e;">{letter}</span> '
        elif text.count(letter) == 1:
            result += f'<span style=" font-weight:600; color:#000000;">{letter}</span> '
        else:
            result += f'<span style=" font-weight:600; color:#d02222 ;">{letter}</span> '
    return result


def to_letter(int: int) -> str:
    return chr(int+65)


def gui_main(args):
    app = QApplication()
    window = EnigmaWindow(args)
    window.show()
    return app.exec_()
