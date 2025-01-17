from PySide2.QtWidgets import QLabel, QListWidget, QPushButton, QStyle
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QDialog
from PySide2.QtWidgets import QListWidgetItem, QMessageBox, QFileDialog
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


def information_dialog(text, title):

    """Show information dialog to user with set text and title"""

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def compleated():
    information_dialog(
        text="Your encryption has been successfully ended",
        title="Encyryption compleated"
    )


def def_config_change():
    information_dialog(
        text="Your default configuration has been changed",
        title="Default configuration changed"
    )


def default_setting_change():
    information_dialog(
        text="Your default settings configuration has been changed",
        title="Setiings configuration changed"
    )


def add_rotor_dialog(data):
    msg = CustomDialog(data)
    msg.setWindowTitle("Add rotor")

    return msg.exec_()


def file_dialog(name_filters=None, any_file=False):

    file_dialog = QFileDialog()
    if any_file is True:
        file_dialog.setFileMode(QFileDialog.AnyFile)
    else:
        file_dialog.setFileMode(QFileDialog.ExistingFile)
    if name_filters is not None:
        file_dialog.setNameFilters(name_filters)
    file_dialog.setViewMode(QFileDialog.Detail)
    filename = None

    if file_dialog.exec_() == QDialog.Accepted:
        filename = file_dialog.selectedFiles()

    return filename
