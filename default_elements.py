from reflector_class import Reflector
from rotor_class import Rotor


# Default rotors from original Enigma machine

rotorI = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
rotorII = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rotorIII = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rotorIV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rotorV = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "K")
rotorVI = "JPGVOUMFYQBENHZRDKASXLICTW"
rotorVII = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
rotorVIII = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
rotorBeta = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
rotorGamma = "FSOKANUERHMBTIYCWLQPZXVGJD"

# Default reflectors from original Enigma machine

reflectorUKWB = Reflector([
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
])

reflectorUKWC = Reflector([
    ("A", "R"),
    ("B", "D"),
    ("C", "O"),
    ("E", "J"),
    ("F", "N"),
    ("G", "T"),
    ("H", "K"),
    ("I", "V"),
    ("L", "M"),
    ("P", "W"),
    ("Q", "Z"),
    ("S", "X"),
    ("U", "Y")
])
