from PySide2.QtWidgets import QMessageBox


def show_invalid_input_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Given sign/s is invalid as an input. \n\
Make sure you type ONE upper case English Alphabet letter (A-Z)")
    msg.setWindowTitle("Invalid input")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_invalid_name():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Name is already in use")
    msg.setWindowTitle("Invalid name")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_empty_name():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Name cannot be empty")
    msg.setWindowTitle("Invalid name")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_duplciated_letter_error(letter):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText(f"{letter} is duplicated (each letter should be used\
no more than once)")
    msg.setWindowTitle("Duplicated letter")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_invalid_sign_error(sign):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText(f"{sign} is not a valid sign")
    msg.setWindowTitle("Invalid sign")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_invalid_plugboard_format():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Input is not a valid plugboard format (AB CD...)")
    msg.setWindowTitle("Invalid fromat")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_invalid_rotor_wiring():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Wiring is not valid. Make sure it is in format 'ABCD...Z'\
         and all letter are included")
    msg.setWindowTitle("Invalid wiring")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_invalid_reflector_wiring():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Wiring is not valid. Make sure it is in format 'AB CD...'\
         and all letter are included")
    msg.setWindowTitle("Invalid wiring")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def show_current_use_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Element, that you want to remove is currently in use")
    msg.setWindowTitle("Element in use")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()
