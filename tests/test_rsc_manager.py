from unittest.mock import Mock
from rsc_manager import InvalidDatabaseJSONFileFormat, ResourcesManager
from rsc_manager import InvalidConfJSONFileFormat
import pytest


def testResourceManagerClass(monkeypatch):

    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        }]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')

    assert rsc_man.rsc_path == 'sample_path'

    assert len(rsc_man._default.rotors) == 2
    assert len(rsc_man._default.reflectors) == 1

    assert len(rsc_man._custom.rotors) == 1
    assert len(rsc_man._custom.reflectors) == 1

    assert len(rsc_man._elements.rotors) == 3
    assert len(rsc_man._elements.reflectors) == 2

    assert rsc_man._conf['machine']['rotors'] == ['rotorI',
                                                  'rotorII', 'rotorIII']
    assert rsc_man._conf['machine']['rings'] == 'XQP'
    assert rsc_man._conf['machine']['start_positions'] == 'NDV'
    assert rsc_man._conf['machine']['reflector'] == 'reflectorUKWC'
    assert rsc_man._conf['machine']['plugboard'] == 'AS DF RY'
    assert rsc_man._conf['settings']['double_step'] is True
    assert rsc_man._conf['settings']['space_dist'] == 8


def test_ResourceManager_invalid_default_database(monkeypatch):
    return_data = [
        {
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        }]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    with pytest.raises(InvalidDatabaseJSONFileFormat):
        ResourcesManager('sample_path')


def test_ResourceManager_invalid_custom_database(monkeypatch):
    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
        },
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        }]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    with pytest.raises(InvalidDatabaseJSONFileFormat):
        ResourcesManager('sample_path')


def test_initialize_enigma(monkeypatch):
    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        }]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')
    enigma = rsc_man.initialize_enigma()

    assert len(enigma.rotors) == 3
    assert enigma.rotors[0].name == 'rotorI'
    assert enigma.rotors[0].position == 13
    assert enigma.rotors[0].ring == 23

    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 3
    assert enigma.rotors[1].ring == 16

    assert enigma.rotors[2].name == 'rotorIII'
    assert enigma.rotors[2].position == 21
    assert enigma.rotors[2].ring == 15

    assert enigma.reflector.name == 'reflectorUKWC'

    assert enigma.plugboard.connections == 'AS DF RY'

    assert enigma.double_step is True

    assert enigma.space_dist == 8


def test_initialize_enigma_invaid_format(monkeypatch):
    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },


        }]

    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')

    with pytest.raises(InvalidConfJSONFileFormat):
        rsc_man.initialize_enigma()


def test_initialize_enigma_from_file(monkeypatch):
    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        },
        {
            "machine": {
                "rotors": [
                    'rotorIII',
                    'rotorII',
                    'rotorI',
                ],
                "rings": "AAA",
                "start_positions": "ABC",
                "reflector": "reflectorUKWB",
                "plugboard": "RE"
            },
            "settings": {
                "double_step": False,
                "space_dist": 3
            }
        }
        ]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')
    enigma = rsc_man.initailze_enigma_with_file('path')

    assert len(enigma.rotors) == 3
    assert enigma.rotors[0].name == 'rotorIII'
    assert enigma.rotors[0].position == 0
    assert enigma.rotors[0].ring == 0

    assert enigma.rotors[1].name == 'rotorII'
    assert enigma.rotors[1].position == 1
    assert enigma.rotors[1].ring == 0

    assert enigma.rotors[2].name == 'rotorI'
    assert enigma.rotors[2].position == 2
    assert enigma.rotors[2].ring == 0

    assert enigma.reflector.name == 'reflectorUKWB'

    assert enigma.plugboard.connections == 'RE'

    assert enigma.double_step is False

    assert enigma.space_dist == 3


def test_initialize_enigma_from_file_invalid_format(monkeypatch):
    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        },
        {
            "machine": {
                "rotors": [
                    'rotorIII',
                    'rotorII',
                    'rotorI',
                ],
                "rings": "AAA",
            },
            "settings": {
                "double_step": False,
                "space_dist": 3
            }
        }
        ]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')

    with pytest.raises(InvalidConfJSONFileFormat):
        rsc_man.initailze_enigma_with_file('')


def test_get_settings_from_enigma(monkeypatch):
    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        },
        {
            "machine": {
                "rotors": [
                    'rotorIII',
                    'rotorII',
                    'rotorI',
                ],
                "rings": "AAA",
                "start_positions": "ABC",
                "reflector": "reflectorUKWB",
                "plugboard": "RE"
            },
            "settings": {
                "double_step": False,
                "space_dist": 3
            }
        }
        ]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')

    enigma = rsc_man.initailze_enigma_with_file('path')

    settings = rsc_man.get_settings_from_enigma(enigma)

    assert settings['machine']['rotors'] == ['rotorI',
                                             'rotorII', 'rotorIII']
    assert settings['machine']['rings'] == 'XQP'
    assert settings['machine']['start_positions'] == 'NDV'
    assert settings['machine']['reflector'] == 'reflectorUKWC'
    assert settings['machine']['plugboard'] == 'AS DF RY'
    assert settings['settings']['double_step'] is False
    assert settings['settings']['space_dist'] == 3


def test_get_conf_from_enigma(monkeypatch):

    return_data = [
        {
            "rotors": [
                {
                    'name': 'rotorI',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                },

                {
                    'name': 'rotorII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'O'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWB",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                }
            ]},
        {
            "rotors": [
                {
                    'name': 'rotorIII',
                    'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
                    'indentations': 'DE'
                }
            ],
            "reflectors": [
                {
                    "name": "reflectorUKWC",
                    "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
                },
            ]},
        {
            "machine": {
                "rotors": [
                    'rotorI',
                    'rotorII',
                    'rotorIII',
                ],
                "rings": "XQP",
                "start_positions": "NDV",
                "reflector": "reflectorUKWC",
                "plugboard": "AS DF RY"
            },
            "settings": {
                "double_step": True,
                "space_dist": 8
            }

        },
        {
            "machine": {
                "rotors": [
                    'rotorIII',
                    'rotorII',
                    'rotorI',
                ],
                "rings": "AAA",
                "start_positions": "ABC",
                "reflector": "reflectorUKWB",
                "plugboard": "RE"
            },
            "settings": {
                "double_step": False,
                "space_dist": 3
            }
        }
        ]
    test_mock = Mock(side_effect=return_data)
    monkeypatch.setattr("rsc_manager.read_from_json", test_mock)

    rsc_man = ResourcesManager('sample_path')

    enigma = rsc_man.initailze_enigma_with_file('path')

    settings = rsc_man.get_conf_from_enigma(enigma)

    assert settings['machine']['rotors'] == ['rotorIII',
                                             'rotorII', 'rotorI']
    assert settings['machine']['rings'] == 'AAA'
    assert settings['machine']['start_positions'] == 'ABC'
    assert settings['machine']['reflector'] == 'reflectorUKWB'
    assert settings['machine']['plugboard'] == 'RE'
    assert settings['settings']['double_step'] is True
    assert settings['settings']['space_dist'] == 8
