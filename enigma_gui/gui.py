from PySide2.QtWidgets import QApplication, QFileDialog, QDialog
from PySide2.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from enigma_gui.dialog_windows import CustomDialog
from enigma_gui.table_models import StepsTableModel, ConifgTableModel
from enigma_gui.main_window import Ui_MainWindow
from enigma_gui.functions import plugboard_to_str, str_to_plugboard, to_number
from rsc_manager import Configuration, ResourcesManager
from copy import deepcopy
import os
from functools import partial


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class EnigmaWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        cwd = os.getcwd()
        rsc_path = f"{cwd}/rsc"

        self.index = None
        self.ui = Ui_MainWindow()
        self.input = None
        self.output = f"{cwd}/result.txt"
        self.config = f"{cwd}/rsc/config.json"
        self.rsc = ResourcesManager(rsc_path)
        self.run_conf = Configuration(self.rsc.conf.data)
        self.temp = deepcopy(self.run_conf)
        self.enigma = self.rsc.initialize_enigma()
        self.space_info = 5
        self.double_step = False

        data = [[rotor.name, chr(rotor.position+65), rotor.ring]
                for rotor in self.enigma.rotors]
        plugboard_text = plugboard_to_str(self.run_conf.plugboard)

        self.ui.setupUi(self)

        self.ui.enc_by_letter_act.triggered.connect(partial(self.change_pg, 0))
        self.ui.change_config_act.triggered.connect(partial(self.change_pg, 1))
        self.ui.settings_act.triggered.connect(partial(self.change_pg, 2))
        self.ui.en_from_file_act.triggered.connect(partial(self.change_pg, 3))
        self.ui.a_r_rotor_act.triggered.connect(partial(self.change_pg, 4))
        self.ui.a_r_reflector_act.triggered.connect(partial(self.change_pg, 5))

        self.ui.encrypt_button.clicked.connect(self.encrypt_letter)

        self.ui.brow_input_butt.clicked.connect(partial(self.brow_file, "i"))
        self.ui.brow_output_butt.clicked.connect(partial(self.brow_file, "o"))
        self.ui.brow_config_butt.clicked.connect(partial(self.brow_file, "c"))
        self.ui.encrypt_file_button.clicked.connect(self.encrypt_file)

        self.ui.up_button.clicked.connect(self.rotor_swap_up)
        self.ui.down_button.clicked.connect(self.rotor_swap_down)
        self.ui.remove_button.clicked.connect(self.remove_rotor)
        self.ui.add_button.clicked.connect(self.add_rotor)
        self.ui.set_plugboard_button.clicked.connect(self.set_plugboard)
        self.ui.save_conf_button.clicked.connect(self.save_conf)
        self.ui.save_init_conf_button.clicked.connect(self.save_init_conf)

        self.ui.space_info.valueChanged.connect(self.change_space)
        self.ui.is_double_step.stateChanged.connect(self.change_double_step)

        self.ui.ring_comboBox.activated.connect(self.change_ring)
        self.ui.pos_comboBox.activated.connect(self.change_pos)
        self.ui.reflector_comboBox.activated.connect(self.change_reflector)

        self.ui.add_ref_mod_butt.clicked.connect(self.add_ref_model)
        self.ui.add_mod_ref.clicked.connect(self.add_mod_ref)
        self.ui.rem_ref_mod_button.clicked.connect(self.rem_mod_ref)
        self.ui.modify_ref_button.clicked.connect(self.modify_reflector)
        self.ui.cancel_add_ref.clicked.connect(self.cancel_ref_add)

        self.ui.mod_rotor_butt.clicked.connect(self.modify_rotor_model)
        self.ui.add_rotor_mod.clicked.connect(self.add_rotor_model)
        self.ui.add_mod_rotor.clicked.connect(self.add_this_rotor_model)
        self.ui.cancel_add_rotor.clicked.connect(self.cancel_rotor_add)
        self.ui.rem_rotor_mod.clicked.connect(self.remove_rotor_model)

        self.ui.stack.setCurrentIndex(0)
        self.ui.current_config.setModel(ConifgTableModel(data))
        self.ui.reflector_name.setText(self.enigma.reflector.name)
        self.ui.plugboard_connections.setText(plugboard_text)

        self.ui.space_info.setValue(self.space_info)

        self.ui.output_file_name.setText(self.output)
        self.ui.config_file_name.setText(self.config)

        self.ui.pos_comboBox.addItems(alphabet)
        self.ui.ring_comboBox.addItems(alphabet)
        self.ui.reflector_comboBox.addItems(self.rsc.elements.reflectors)
        self.ui.plugboard_line.setText(plugboard_text)
        self.ui.stack2.setCurrentIndex(0)
        self.setupRotors()

        self.ui.stack3.setCurrentIndex(0)
        self.setup_rotors_models()

        self.ui.stack4.setCurrentIndex(0)
        self.setup_reflectors_models()

    def remove_rotor_model(self):
        self.rsc.custom.remove_rotor(self.index)
        self.setup_rotors_models()
        self.ui.stack3.setCurrentIndex(0)

    def cancel_rotor_add(self):
        self.ui.stack.setCurrentIndex(0)
        self.ui.rotor_name.clear()
        self.ui.rotor_wiring.clear()
        self.ui.rotor_indentation.clear()

    def add_this_rotor_model(self):
        name = self.ui.rotor_name.text()
        wiring = self.ui.rotor_wiring.text()
        indentation = self.ui.rotor_indentation.text()
        self.rsc.custom.add_rotor(name, wiring, indentation)
        self.ui.stack3.setCurrentIndex(0)
        self.setup_rotors_models()
        self.ui.rotor_name.clear()
        self.ui.rotor_wiring.clear()
        self.ui.rotor_indentation.clear()

    def add_rotor_model(self):
        self.ui.stack3.setCurrentIndex(2)

    def modify_rotor_model(self):
        name = self.ui.rotor_name_2.text()
        wiring = self.ui.rotor_wiring_2.text()
        indentation = self.ui.rotor_indentation_2.text()
        index = self.index
        self.rsc.custom.modify_rotor(index, name, wiring, indentation)
        self.setup_rotors_models()

    def setup_rotors_models(self):
        self.ui.rotors_list_2.clear()
        rotors = self.rsc.custom.data["rotors"]
        for i, rotor in enumerate(rotors):
            item = QListWidgetItem(rotor["name"])
            self.ui.rotors_list_2.addItem(item)
            item.position = i
        self.ui.rotors_list_2.itemClicked.connect(self.display_rotor_model_info)

    def display_rotor_model_info(self, item):
        self.index = item.position
        self.ui.stack3.setCurrentIndex(1)
        self.ui.rotor_name_2.setText(item.text())
        self.ui.rotor_wiring_2.setText(self.rsc.custom.data["rotors"][item.position]["wiring"])
        self.ui.rotor_indentation_2.setText(self.rsc.custom.data["rotors"][item.position]["indentation"])

    def modify_reflector(self):
        name = self.ui.reflector_mod_name.text()
        wiring = str_to_plugboard(self.ui.reflector_mod_wiring.text())
        index = self.index
        self.rsc.custom.modify_reflector(index, name, wiring)
        self.setup_reflectors_models()

    def add_mod_ref(self):
        name = self.ui.reflector_mod_name_2.text()
        wiring = str_to_plugboard(self.ui.reflector_mod_wiring_2.text())
        self.rsc.custom.add_reflector(name, wiring)
        self.ui.stack4.setCurrentIndex(0)
        self.setup_reflectors_models()
        self.ui.reflector_mod_name_2.clear()
        self.ui.reflector_mod_wiring_2.clear()

    def rem_mod_ref(self):
        self.rsc.custom.remove_reflector(self.index)
        self.setup_reflectors_models()
        self.ui.reflector_mod_name.clear()
        self.ui.reflector_mod_wiring.clear()

    def setup_reflectors_models(self):
        self.ui.reflectors_list.clear()
        reflector = self.rsc.custom.data["reflectors"]
        for i, reflector in enumerate(reflector):
            item = QListWidgetItem(reflector["name"])
            self.ui.reflectors_list.addItem(item)
            item.position = i
        self.ui.reflectors_list.itemClicked.connect(self.display_reflector_model_info)

    def cancel_ref_add(self):
        self.ui.stack4.setCurrentIndex(1)
        self.ui.reflector_mod_name_2.clear()
        self.ui.reflector_mod_wiring_2.clear()

    def add_ref_model(self):
        self.ui.stack4.setCurrentIndex(2)

    def display_reflector_model_info(self, item):
        self.index = item.position
        self.ui.stack4.setCurrentIndex(1)
        self.ui.reflector_mod_name.setText(item.text())
        # it works because plugboard has the same format like reflectro wiring
        self.ui.reflector_mod_wiring.setText(plugboard_to_str(self.rsc.custom.data["reflectors"][item.position]["wiring"]))

    def reload(self):
        pass

    def change_double_step(self):
        self.enigma.change_double_step()
        self.double_step = True

    def change_space(self):
        self.space_info = self.ui.space_info.value()

    def change_pg(self, page_number):
        self.enigma = self.rsc.initialize_enigma(self.run_conf)
        plugboard_text = plugboard_to_str(self.run_conf.plugboard)
        data = [[rotor.name, chr(rotor.position+65), rotor.ring]
                for rotor in self.enigma.rotors]
        self.set_page(page_number)
        self.temp = deepcopy(self.run_conf)
        if len(self.enigma.rotors) != 3:
            self.ui.is_double_step.setEnabled(False)
        if len(self.enigma.rotors) == 3:
            self.ui.is_double_step.setEnabled(True)
        self.ui.reflector_comboBox.setCurrentText(self.run_conf.reflector)
        self.ui.space_info.setValue(self.space_info)
        self.ui.plugboard_connections.setText(plugboard_text)
        self.ui.current_config.setModel(ConifgTableModel(data))
        self.ui.plugboard_line.setText(plugboard_text)
        self.ui.stack2.setCurrentIndex(0)
        self.setupRotors()

    def encrypt_letter(self):
        letter = self.ui.letter_input.text()
        self.ui.letter_input.clear()
        cipher_text = self.ui.cipher_text.text()
        if self.enigma.coded_letters_number == self.space_info:
            self.enigma.zero_coded_letters_number()
            cipher_text += " "
        cipher_letter, steps_data = self.enigma.code_letter(letter)
        cipher_text += cipher_letter

        new_data = [[rotor.name, chr(rotor.position+65), rotor.ring]
                    for rotor in self.enigma.rotors]

        self.ui.steps_table.setModel(StepsTableModel(self.generate_labels(), steps_data))
        self.ui.current_config.setModel(ConifgTableModel(data=new_data))
        self.ui.steps_table.horizontalHeader().hide()
        self.ui.cipher_text.setText(cipher_text)

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

    def clear_rotors(self):
        self.ui.rotors_list.clear()

    def rotor_swap_up(self):
        if self.index is None:
            return None
        self.temp.move_rotor_up(self.index)
        self.clear_rotors()
        self.setupRotors()

        # probably it wil be googd idea to connect it with display_rotors_info
        if self.index != 0:
            self.ui.rotors_list.setCurrentRow(self.index-1)
            self.index -= 1
        else:
            self.ui.rotors_list.setCurrentRow(self.index)

    def rotor_swap_down(self):
        if self.index is None:
            return None
        self.temp.move_rotor_down(self.index)
        self.clear_rotors()
        self.setupRotors()
        if self.index != len(self.temp.rotors)-1:
            self.ui.rotors_list.setCurrentRow(self.index+1)
            self.index += 1
        else:
            self.ui.rotors_list.setCurrentRow(self.index)

    def setupRotors(self):
        self.ui.rotors_list.clear()
        rotors = self.temp.rotors
        for i, rotor in enumerate(rotors):
            item = QListWidgetItem(rotor)
            self.ui.rotors_list.addItem(item)
            item.position = i
        self.ui.rotors_list.itemClicked.connect(self.display_rotor_info)

    def set_plugboard(self):
        str_plugboard = self.ui.plugboard_line.text()
        plugboard = str_to_plugboard(str_plugboard)
        self.temp.set_plugboard(plugboard)

    def display_rotor_info(self, item):
        self.index = int(item.position)
        self.ui.stack2.setCurrentIndex(1)
        self.ui.ring_comboBox.setCurrentIndex(to_number(self.temp.rings[self.index]))
        self.ui.pos_comboBox.setCurrentIndex(to_number(self.temp.positions[self.index]))

    def remove_rotor(self):
        self.temp.remove_rotor(self.index)
        self.index = None
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

    def change_ring(self):
        new_ring = str(self.ui.ring_comboBox.currentText())
        self.temp.change_ring(self.index, new_ring)

    def change_pos(self):
        new_pos = str(self.ui.pos_comboBox.currentText())
        self.temp.change_position(self.index, new_pos)

    def change_reflector(self):
        new_reflector = str(self.ui.reflector_comboBox.currentText())
        self.temp.change_reflector(new_reflector)

    def save_conf(self):
        self.run_conf = deepcopy(self.temp)
        show_config_change_dialog()

    def save_init_conf(self):
        self.temp.save_conf(self.rsc.conf)
        show_init_config_change_dialog()

    def encrypt_file(self):
        self.rsc.conf.get_temp_config_from_file(self.config)
        sub_enigma = self.rsc.initialize_enigma(double_step=self.double_step)
        sub_enigma.code_file(self.input, self.output, self.space_info)
        show_compleated_dialog()

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


def gui_main(args):
    app = QApplication(args)
    window = EnigmaWindow()
    window.show()
    return app.exec_()
