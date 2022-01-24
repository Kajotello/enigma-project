from PySide2.QtWidgets import QMessageBox


def error_message(text, title):

    """Show error dialog"""

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Ok)

    return msg.exec_()


def invalid_input():
    error_message(
        text="Given sign/s is invalid as an input. \n\
Make sure you type ONE upper case English Alphabet letter (A-Z)",
        title="Invalid input"
    )


def name_in_use():
    error_message(
        text="Name is already in use",
        title="Invalid name"
    )


def empty_name():
    error_message(
        text="Name cannot be empty",
        title="Invalid name"
    )


def duplciated_letter():
    error_message(
        text="Duplicated letter. Each letter should be used \
no more than once)",
        title="Duplicated letter"
    )


def invalid_sign():
    error_message(
        text="One of the sign in input is not valid",
        title="Invalid sign"
    )


def invalid_plugboard_format():
    error_message(
        text="Input is not a valid plugboard format (AB CD...)",
        title="Invalid fromat"
    )


def invalid_rotor_wiring():
    error_message(
        text="Wiring is not valid. Make sure it is in format 'ABCD...Z' \
and all letter are included",
        title="Invalid wiring"
    )


def invalid_reflector_wiring():
    error_message(
        text="Wiring is not valid. Make sure it is in format 'AB CD...' \
and all letter are included",
        title="Invalid wiring"
    )


def current_use_error():
    error_message(
        text="Element, that you want to modify/remove, is currently in use",
        title="Element in use"
    )


def failed_elements_load_duplicated_name():
    error_message(
        text="Some of the elements you want to load hava the same name as \
currently existing at database. Solve conflict and try again",
        title="Name conflict"
    )


def failed_elements_load():
    error_message(
        text="Load from file filed. Check is file exist \
and have the right format",
        title="Loading fail"
    )


def indentations_invalid_sign():
    error_message(
        text="One or more sign in indentations in not valid. \
Make sure you type upper case English Alphabet letter (A-Z)",
        title="Invalid sign"
    )


def indentations_duplicated_letter():
    error_message(
        text="Two lettters given by you as indentations are same. \
You must type two different letters",
        title="Duplicated letter"
    )


def indenations_invalid_format():
    error_message(
        text="Format of indentations is not valid. It should be \
one or two letters without any spaces",
        title="Invalid indentation format"
    )


def rotor_not_in_database():
    error_message(
        text="One or more rotors from configuration are not found in \
database",
        title="Rotor not in database"
    )


def reflector_not_in_database():
    error_message(
        text="Reflector from configuration are not found in \
database",
        title="Reflector not in database"
    )


def not_a_JSON():
    error_message(
        text="File must be in JSON (.json) format",
        title="JSON required"
    )


def invalid_conf_JSON():
    error_message(
        text="Format of given JSON file is not compatible. \
Check it in documentation",
        title="Invalid configuration JSON format "
    )


def invalid_db_JSON():
    error_message(
        text="Format of given JSON file is not compatible. \
Check it in documentation",
        title="Invalid database JSON format "
    )


def invalid_sign_in_file():
    error_message(
        text="Encrytpion failed - file have unsupported sign/s. \
Only uppercase letters of English alphabet (without spaces)\
is allowed",
        title="Invalid sign in file"
    )


def not_file_with_name():
    error_message(
        text="File with that name does not exist",
        title="Invalid file name"
    )


def file_not_selected_yet():
    error_message(
        text="File with input hasn't been selected",
        title="No input file name"
    )
