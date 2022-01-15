from PySide2.QtWidgets import QLabel, QListWidget, QPushButton, QStyle
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QDialog
from PySide2.QtWidgets import QListWidgetItem, QMessageBox
from functools import partial


class CustomDialog(QDialog):
    def __init__(self, data):
        super().__init__()

        self.rotor_pos = -1
        self.add_button = QPushButton("Add")
        self.cancel_button = QPushButton("Cancel")
        self.add_button.clicked.connect(self.my_done)
        self.cancel_button.clicked.connect(partial(self.done, -1))
        pixmapi = getattr(QStyle, 'SP_DialogApplyButton')
        icon = self.style().standardIcon(pixmapi)
        self.add_button.setIcon(icon)
        pixmapi = getattr(QStyle, 'SP_DialogCancelButton')
        icon = self.style().standardIcon(pixmapi)
        self.cancel_button.setIcon(icon)

        self.layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()
        message = QLabel("Choose rotor to add:")
        self.available_rotors = QListWidget()
        for i, rotor in enumerate(data.rotors):
            item = QListWidgetItem(rotor)
            item.pos = i
            self.available_rotors.addItem(item)
        self.available_rotors.itemClicked.connect(self.on_rotor_select)
        self.horizontal_layout.addWidget(self.add_button)
        self.horizontal_layout.addWidget(self.cancel_button)
        self.layout.addWidget(message)
        self.layout.addWidget(self.available_rotors)
        self.layout.addLayout(self.horizontal_layout)

        self.setLayout(self.layout)

    def on_rotor_select(self, item):
        self.rotor_pos = item.pos

    def my_done(self):
        self.done(self.rotor_pos)


def compleated():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Your encryption has been successfully ended.")
    msg.setWindowTitle("Encyryption compleated")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def init_config_change():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Your initial configuration has been changed.")
    msg.setWindowTitle("Initial configuration changed")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def config_change():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Your current configuration has been changed.")
    msg.setWindowTitle("Configuration changed")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def add_rotor(data):
    msg = CustomDialog(data)
    msg.setWindowTitle("Add rotor")

    return msg.exec_()
