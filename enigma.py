from rotors import rotorI, rotorII, rotorIII
from rotor_class import Rotor
from reflectors import reflectorUKWB
from reflectors import Reflector
from enigma_class import Enigma

rotor_1st = Rotor(rotorI, "Q")
rotor_2nd = Rotor(rotorII, "E")
rotor_3rd = Rotor(rotorIII, "V")
rotors = [rotor_1st,  rotor_2nd, rotor_3rd]
reflector = Reflector(reflectorUKWB)
enigma = Enigma(rotors, reflector, ("A", "D", "A"), ("A", "B", "A"))

list = []
while True:
    letter = input("Give letter to encrypt: ")
    list.append(enigma.code_letter(letter))
    print(list)
