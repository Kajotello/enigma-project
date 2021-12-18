from rotors import rotorI, rotorII, rotorIII
from rotor_class import Rotor
from reflectors import reflectorUKWB
from reflectors import Reflector
from enigma_class import Enigma

rotor_1st = Rotor(rotorI, "N")
rotor_2nd = Rotor(rotorII, "O")
rotor_3rd = Rotor(rotorIII, "S")
rotors = [rotor_1st,  rotor_2nd, rotor_3rd]
reflector = Reflector(reflectorUKWB)
enigma = Enigma(rotors, reflector, ("Z", "F", "P"))

list = []
while True:
    enigma.rotors[-1].rotate()
    letter = input("Give letter to encrypt: ")
    list.append(enigma.code_letter(letter))
    print(list)
