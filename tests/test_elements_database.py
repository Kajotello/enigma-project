from elements_database import CustomElementsDatabase, InvalidElementsDataError
from elements_database import NotUniqueKeyError
from rsc_manager import ElementsDatabase
from elements_database import NameInUseError
from elements_database import InvalidNameError
import pytest


def test_ElementsDatabse_class():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database = ElementsDatabase(elements_data)

    assert database._rotors["rotorA"].name == "rotorA"
    assert database._rotors["rotorA"].indentations == [2]
    assert database._rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database._rotors["rotorB"].name == "rotorB"
    assert database._rotors["rotorB"].indentations == [5]
    assert database._rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert database._rotors["rotorC"].name == "rotorC"
    assert database._rotors["rotorC"].indentations == [14]
    assert database._rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database._reflectors["reflectorI"].name == 'reflectorI'
    assert (database._reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database._reflectors["reflectorII"].name == 'reflectorII'
    assert (database._reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_ElementsDatabase_invalid_data():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ]
    }

    with pytest.raises(InvalidElementsDataError):
        ElementsDatabase(elements_data)


def test_ElementsDatabase_rotors():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database = ElementsDatabase(elements_data)

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorB"].name == "rotorB"
    assert database.rotors["rotorB"].indentations == [5]
    assert database.rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"


def test_ElementsDatabase_reflectors():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database = ElementsDatabase(elements_data)

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database.reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database.reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_CustomElementsDatabase():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    assert database.connected_database == connected_database


def test_add_rotor():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.add_rotor('rotorC', 'CDEFGHIJKLMNOPQRSTUVWXYZAB', 'O')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorB"].name == "rotorB"
    assert database.rotors["rotorB"].indentations == [5]
    assert database.rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database.reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database.reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_add_rotor_name_in_use():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    with pytest.raises(NameInUseError):
        database.add_rotor('rotorA', 'CDEFGHIJKLMNOPQRSTUVWXYZAB', 'O')


def test_add_reflector():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.add_reflector('reflectorII',
                           'AY BR CD UH EQ FS GL IP JX KN MO TZ VW')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorB"].name == "rotorB"
    assert database.rotors["rotorB"].indentations == [5]
    assert database.rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database.reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database.reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_remove_rotor():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.remove_rotor('rotorB')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"
    assert database.rotors.get("rotorB", None) is None

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database.reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database.reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_remove_rotor_invalid_key():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    with pytest.raises(InvalidNameError):
        database.remove_rotor('rotorD')


def test_remove_reflector():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.remove_reflector('reflectorI')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database._reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")

    assert database.reflectors.get("reflectorI", None) is None


def test_remove_reflector_invalid_key():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    with pytest.raises(InvalidNameError):
        database.remove_reflector('reflectorIII')


def test_modify_reflector():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.modify_reflector('reflectorI', 'new_reflector',
                              'AW BR CU DH EQ FG SL IP JX KN MO TZ VY')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database._reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")

    assert database.reflectors["new_reflector"].name == 'new_reflector'
    assert (database._reflectors["new_reflector"].wiring ==
           "AW BR CU DH EQ FG SL IP JX KN MO TZ VY")


def test_modify_relflector_with_same_name():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.modify_reflector('reflectorI', 'reflectorI',
                              'AW BR CU DH EQ FG SL IP JX KN MO TZ VY')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database._reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database._reflectors["reflectorI"].wiring ==
           "AW BR CU DH EQ FG SL IP JX KN MO TZ VY")


def test_modify_reflector_name_in_use_error():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    with pytest.raises(NameInUseError):
        database.modify_reflector('reflectorI', 'reflectorII',
                                  'AW BR CU DH EQ FG SL IP JX KN MO TZ VY')


def test_modify_rotor():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.modify_rotor('rotorA', 'new_rotor',
                          'DEFGHIJKLMNOPQRSTUVWXYZABC', 'Q')

    assert database.rotors["new_rotor"].name == "new_rotor"
    assert database.rotors["new_rotor"].indentations == [16]
    assert database.rotors["new_rotor"].wiring == "DEFGHIJKLMNOPQRSTUVWXYZABC"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database._reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database._reflectors["reflectorI"].wiring ==
           "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")


def test_modify_rotor_with_same_name():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    database.modify_rotor('rotorA', 'rotorA',
                          'DEFGHIJKLMNOPQRSTUVWXYZABC', 'Q')

    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [16]
    assert database.rotors["rotorA"].wiring == "DEFGHIJKLMNOPQRSTUVWXYZABC"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database._reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database._reflectors["reflectorI"].wiring ==
           "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")


def test_modify_rotor_name_in_use_error():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    connected_database = ElementsDatabase()
    database = CustomElementsDatabase(connected_database, elements_data)
    with pytest.raises(NameInUseError):
        database.modify_rotor('rotorA', 'rotorC',
                              'DEFGHIJKLMNOPQRSTUVWXYZABC', 'Q')


def test_check_rotor_with_second_database_key_in_custom_db():

    elements_data1 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorII",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorW",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorQ",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    database1 = ElementsDatabase(elements_data1)
    database2 = CustomElementsDatabase(database1, elements_data2)
    with pytest.raises(NameInUseError):
        database2.check_rotor_key_with_second_database('rotorI')


def test_check_rotor_with_second_database_key_in_connected_db():
    elements_data1 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorII",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorW",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorQ",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    database1 = ElementsDatabase(elements_data1)
    database2 = CustomElementsDatabase(database1, elements_data2)
    with pytest.raises(NameInUseError):
        database2.check_rotor_key_with_second_database('rotorA')


def test_check_rotor_key_in_second_database():
    elements_data1 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorII",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorW",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorQ",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    database1 = ElementsDatabase(elements_data1)
    database2 = CustomElementsDatabase(database1, elements_data2)
    with pytest.raises(NameInUseError):
        database2.check_rotor_key_in_second_database('rotorA')


def test_check_reflector_with_second_database_key_in_first_db():
    elements_data1 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorII",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorW",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorQ",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    database1 = ElementsDatabase(elements_data1)
    database2 = CustomElementsDatabase(database1, elements_data2)
    with pytest.raises(NameInUseError):
        database2.check_reflector_key_with_second_database('reflectorW')


def test_check_reflector_with_second_database_key_in_connected_db():
    elements_data1 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorII",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorW",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorQ",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    database1 = ElementsDatabase(elements_data1)
    database2 = CustomElementsDatabase(database1, elements_data2)
    with pytest.raises(NameInUseError):
        database2.check_reflector_key_with_second_database('reflectorI')


def test_check_reflector_key_in_second_database():
    elements_data1 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorII",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorW",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },
            {
                "name": "reflectorQ",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }
    database1 = ElementsDatabase(elements_data1)
    database2 = CustomElementsDatabase(database1, elements_data2)
    with pytest.raises(NameInUseError):
        database2.check_reflector_key_in_second_database('reflectorI')


def test_add_database():

    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },

        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },

        ],
        "reflectors": [
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database1 = ElementsDatabase(elements_data)
    database2 = ElementsDatabase(elements_data2)
    database = database1 + database2

    assert isinstance(database, CustomElementsDatabase) is False
    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorB"].name == "rotorB"
    assert database.rotors["rotorB"].indentations == [5]
    assert database.rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database.reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database.reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_add_database_with_same_key():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },

        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },

        ],
        "reflectors": [
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database1 = ElementsDatabase(elements_data)
    database2 = ElementsDatabase(elements_data2)
    with pytest.raises(NotUniqueKeyError):
        database1 + database2


def test_add_ElementsDatabase_to_CustomElementsDatabase():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },

        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },

        ],
        "reflectors": [
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database1 = ElementsDatabase(elements_data)
    database2 = CustomElementsDatabase(database1, elements_data2)
    database = database1 + database2

    assert isinstance(database, CustomElementsDatabase) is False
    assert database.rotors["rotorA"].name == "rotorA"
    assert database.rotors["rotorA"].indentations == [2]
    assert database.rotors["rotorA"].wiring == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert database.rotors["rotorB"].name == "rotorB"
    assert database.rotors["rotorB"].indentations == [5]
    assert database.rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert database.rotors["rotorC"].name == "rotorC"
    assert database.rotors["rotorC"].indentations == [14]
    assert database.rotors["rotorC"].wiring == "CDEFGHIJKLMNOPQRSTUVWXYZAB"

    assert database.reflectors["reflectorI"].name == 'reflectorI'
    assert (database.reflectors["reflectorI"].wiring ==
            "AW BR CU DH EQ FS GL IP JX KN MO TZ VY")

    assert database.reflectors["reflectorII"].name == 'reflectorII'
    assert (database.reflectors["reflectorII"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")


def test_add_two_CustomElementsDatabase():
    elements_data = {
        "rotors": [
            {
                "name": "rotorA",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "C"
            },
            {
                "name": "rotorC",
                "wiring": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                "indentations": "O"
            },
        ],
        "reflectors": [
            {
                "name": "reflectorI",
                "wiring": "AW BR CU DH EQ FS GL IP JX KN MO TZ VY",
            },

        ]
    }

    elements_data2 = {
        "rotors": [
            {
                "name": "rotorB",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },

        ],
        "reflectors": [
            {
                "name": "reflectorII",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    elements_data3 = {
        "rotors": [
            {
                "name": "rotorO",
                "wiring": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                "indentations": "F"
            },

        ],
        "reflectors": [
            {
                "name": "reflectorY",
                "wiring": "AY BR CD UH EQ FS GL IP JX KN MO TZ VW",
            },
        ]
    }

    database1 = ElementsDatabase(elements_data)
    database2 = CustomElementsDatabase(database1, elements_data2)
    database3 = CustomElementsDatabase(database1, elements_data3)
    new_database = database2 + database3

    assert isinstance(new_database, CustomElementsDatabase) is True
    assert new_database.rotors["rotorB"].name == "rotorB"
    assert new_database.rotors["rotorB"].indentations == [5]
    assert new_database.rotors["rotorB"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert new_database.rotors["rotorO"].name == "rotorO"
    assert new_database.rotors["rotorO"].indentations == [5]
    assert new_database.rotors["rotorO"].wiring == "BCDEFGHIJKLMNOPQRSTUVWXYZA"

    assert new_database.reflectors["reflectorII"].name == 'reflectorII'
    assert (new_database.reflectors["reflectorII"].wiring ==
            "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")

    assert new_database.reflectors["reflectorY"].name == 'reflectorY'
    assert (new_database.reflectors["reflectorY"].wiring ==
           "AY BR CD UH EQ FS GL IP JX KN MO TZ VW")
