from enigma_classes.enigma_class import Enigma
from elements_database import ElementsDatabase


def test_Enigma_class():

    conf_data = {
        "machine": {
            "rotors": [
                "rotorIII",
                "rotorII",
                "rotorI",
            ],
            "rings": "BCD",
            "start_positions": "DEA",
            "reflector": "reflectorUKWB",
            "plugboard": "AS"
        },
        "settings": {
            "double_step": False,
            "space_dist": 5
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elements_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elements_database)

    assert len(enigma._rotors) == 3
    assert enigma._rotors[0].name == 'rotorIII'
    assert enigma._rotors[0].ring == 1
    assert enigma._rotors[0].position == 3
    assert enigma._rotors[1].name == 'rotorII'
    assert enigma._rotors[1].ring == 2
    assert enigma._rotors[1].position == 4
    assert enigma._rotors[2].name == 'rotorI'
    assert enigma._rotors[2].ring == 3
    assert enigma._rotors[2].position == 0
    assert enigma._reflector == elements_database.reflectors['reflectorUKWB']
    assert enigma._plugboard.connections == 'AS'
    assert enigma._plugboard.plugboard_dict == {0: 18, 18: 0}
    assert enigma._double_step is False
    assert enigma._space_dist == 5
    assert enigma._letter_counter == 0
    assert enigma._database == elements_database


def test_rotors_property():

    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "DC"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)

    assert len(enigma._rotors) == 4
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].ring == 18
    assert enigma.rotors[1].position == 0
    assert enigma.rotors[2].name == 'rotorI'
    assert enigma.rotors[2].ring == 0
    assert enigma.rotors[2].position == 0
    assert enigma.rotors[3].name == 'rotorIII'
    assert enigma.rotors[3].ring == 3
    assert enigma.rotors[3].position == 0


def test_reflectors_property():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "DC"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)

    enigma.reflector == elemnts_database.reflectors['reflectorUKWC']


def test_plugboard_property():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)

    assert enigma.plugboard.plugboard_dict == {0: 24, 24: 0}
    assert enigma.plugboard.connections == 'AY'


def test_double_step_property():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI"
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)

    assert enigma.double_step is True


def test_space_dist_property():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    assert enigma.space_dist == 2


def test_letter_counter_property():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    assert enigma.letter_counter == 0


def test_database_property():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    assert enigma.database == elemnts_database


def test_update_database():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }

    new_database = {
        "rotors": [
            {
                "name": "torotA",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            }
        ],

        "reflectors": [

            {
                "name": "reflectorUKWS",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.set_database(new_database)
    assert enigma.database == new_database


def test_set_plugoard():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.set_plugboard('BC ZY')
    assert enigma.plugboard.plugboard_dict == {1: 2, 2: 1, 25: 24, 24: 25}
    assert enigma.plugboard.connections == 'BC ZY'


def test_change_double_step():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI"
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.change_double_step()
    assert enigma.double_step is False


def test_change_reflector():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.change_reflector('reflectorUKWB')
    assert enigma.reflector == elemnts_database.reflectors['reflectorUKWB']


def test_change_position():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": 1,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.change_position(1, 'C')
    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 2
    assert enigma.rotors[1].ring == 18


def test_change_ring():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "AAAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.change_ring(2, 'E')
    assert enigma.rotors[2].name == 'rotorI'
    assert enigma.rotors[2].position == 0
    assert enigma.rotors[2].ring == 4


def test_add_rotor():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
            ],
            "rings": "ZS",
            "start_positions": "BC",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.add_rotor('rotorIII')
    assert len(enigma.rotors) == 3
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 1
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 2
    assert enigma.rotors[1].ring == 18
    assert enigma.rotors[2].name == 'rotorIII'
    assert enigma.rotors[2].position == 0
    assert enigma.rotors[2].ring == 0


def test_remove_rotor():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "ABCD",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.remove_rotor(1)
    assert len(enigma.rotors) == 3
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[1].name == 'rotorI'
    assert enigma.rotors[1].position == 2
    assert enigma.rotors[1].ring == 0
    assert enigma.rotors[2].name == 'rotorIII'
    assert enigma.rotors[2].position == 3
    assert enigma.rotors[2].ring == 3


def test_move_rotor_up():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "ABCD",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.move_rotor_up(2)
    assert len(enigma.rotors) == 4
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[1].name == 'rotorI'
    assert enigma.rotors[1].position == 2
    assert enigma.rotors[1].ring == 0
    assert enigma.rotors[2].name == 'rotorII'
    assert enigma.rotors[2].position == 1
    assert enigma.rotors[2].ring == 18
    assert enigma.rotors[3].name == 'rotorIII'
    assert enigma.rotors[3].position == 3
    assert enigma.rotors[3].ring == 3


def test_move_rotor_up_first_rotor():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "ABCD",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.move_rotor_up(0)
    assert len(enigma.rotors) == 4
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 1
    assert enigma.rotors[1].ring == 18
    assert enigma.rotors[2].name == 'rotorI'
    assert enigma.rotors[2].position == 2
    assert enigma.rotors[2].ring == 0
    assert enigma.rotors[3].name == 'rotorIII'
    assert enigma.rotors[3].position == 3
    assert enigma.rotors[3].ring == 3


def test_move_rotor_down():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "ABCD",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.move_rotor_down(2)
    assert len(enigma.rotors) == 4
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 1
    assert enigma.rotors[1].ring == 18
    assert enigma.rotors[2].name == 'rotorIII'
    assert enigma.rotors[2].position == 3
    assert enigma.rotors[2].ring == 3
    assert enigma.rotors[3].name == 'rotorI'
    assert enigma.rotors[3].position == 2
    assert enigma.rotors[3].ring == 0


def test_move_rotor_down_last_rotor():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "ZSAD",
            "start_positions": "ABCD",
            "reflector": "reflectorUKWC",
            "plugboard": "AY"
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    enigma.move_rotor_down(3)
    assert len(enigma.rotors) == 4
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[0].ring == 25
    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 1
    assert enigma.rotors[1].ring == 18
    assert enigma.rotors[2].name == 'rotorI'
    assert enigma.rotors[2].position == 2
    assert enigma.rotors[2].ring == 0
    assert enigma.rotors[3].name == 'rotorIII'
    assert enigma.rotors[3].position == 3
    assert enigma.rotors[3].ring == 3


def test_code_letter_basic_positions_and_rings():
    conf_data = {
        "machine": {
            "rotors": [
                "rotorI",
                "rotorII",
                "rotorI",
                'rotorIII',
            ],
            "rings": "AAAA",
            "start_positions": "AAAZ",
            "reflector": "reflectorUKWC",
            "plugboard": "",
        },
        "settings": {
            "double_step": True,
            "space_dist": 2
        }
    }

    database = {
        "rotors": [
            {
                "name": "rotorI",
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "indentations": "Q"
            },

            {
                "name": "rotorII",
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "indentations": "E"
            },

            {
                "name": "rotorIII",
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "indentations": "V"
            },
                ],

        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            },

            {
                "name": "reflectorUKWC",
                "wiring": "AF BV CP DJ EI GO HY KR LZ MX NW QT SU"
            }
        ]
    }
    elemnts_database = ElementsDatabase(database)
    enigma = Enigma(conf_data, elemnts_database)
    cipher_letter = enigma.code_letter('D')
    assert cipher_letter[0] == 'J'
    assert cipher_letter[1] == ['D', 'D', 'H', 'Q', 'Q', 'X', 'M', 'C', 'P',
                                'T', 'J', 'J', 'J']


def test_code_letter_with_rotation():
    assert 0 == 1
    # @TODO


def test_code_letter_with_double_step():
    assert 0 == 1
    # @TODO


def test_code_letter_with_pottencial_double_step():
    assert 0 == 1
    # @TODO


def test_code_file():
    assert 0 == 1
    # @TODO
