reflectorUKWB = [
    ("A", "Y"),
    ("B", "R"),
    ("C", "U"),
    ("D", "H"),
    ("E", "Q"),
    ("F", "S"),
    ("G", "L"),
    ("I", "P"),
    ("J", "X"),
    ("K", "N"),
    ("M", "O"),
    ("T", "Z"),
    ("V", "W")
]


# It should't be here, but temporary will be (or maybe should, i will see :)

class Reflector():
    def __init__(self, reflector) -> None:
        reflector_dict = {}
        for pair in reflector:
            first_letter, second_leter = pair
            first_letter = ord(first_letter) - 65
            second_leter = ord(second_leter) - 65
            reflector_dict[first_letter] = second_leter
            reflector_dict[second_leter] = first_letter
        self._reflector_dict = reflector_dict

    @property
    def reflector_dict(self):
        return self._reflector_dict
