from PySide2.QtWidgets import QMessageBox


def invalid_input():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Given sign/s is invalid as an input. \n\
Make sure you type ONE upper case English Alphabet letter (A-Z)")
    msg.setWindowTitle("Invalid input")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def name_in_use():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Name is already in use")
    msg.setWindowTitle("Invalid name")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def empty_name():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Name cannot be empty")
    msg.setWindowTitle("Invalid name")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def duplciated_letter():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Duplicated letter. Each letter should be used\
no more than once)")
    msg.setWindowTitle("Duplicated letter")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def invalid_sign():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("One of the sign in input is not valid")
    msg.setWindowTitle("Invalid sign")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def invalid_plugboard_format():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Input is not a valid plugboard format (AB CD...)")
    msg.setWindowTitle("Invalid fromat")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def invalid_rotor_wiring():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Wiring is not valid. Make sure it is in format 'ABCD...Z'\
         and all letter are included")
    msg.setWindowTitle("Invalid wiring")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def invalid_reflector_wiring():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Wiring is not valid. Make sure it is in format 'AB CD...'\
         and all letter are included")
    msg.setWindowTitle("Invalid wiring")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def current_use_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Element, that you want to remove is currently in use")
    msg.setWindowTitle("Element in use")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def encryption():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Encryption ended with error")
    msg.setWindowTitle("Encryption Error")
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()
