from default_elements import (rotorI, rotorII, rotorIII, rotorIV, rotorV,
                              rotorVI, rotorVII, rotorVIII, rotorBeta,
                              rotorGamma, reflectorUKWB, reflectorUKWC)
from rotor_class import Rotor
from reflector_class import Reflector
from enigma_class import Enigma

rotor_1st = Rotor(rotorI, "Q")
rotor_2nd = Rotor(rotorII, "E")
rotor_3rd = Rotor(rotorIII, "V")
rotors = [rotor_1st,  rotor_2nd, rotor_3rd]
reflector = Reflector(reflectorUKWB)
enigma = Enigma(rotors, reflector, ("J", "K", "C"), ("Q", "Q", "Q"))

list = []
while True:
    letter = input("Give letter to encrypt: ")
    list.append(enigma.code_letter(letter))
    print(list)
