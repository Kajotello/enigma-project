from os import write
from default_elements import (rotorI, rotorII, rotorIII, rotorIV, rotorV,
                              rotorVI, rotorVII, rotorVIII, rotorBeta,
                              rotorGamma, reflectorUKWB, reflectorUKWC)
from plugboard_class import Plugboard
from enigma_class import Enigma
import argparse


parser = argparse.ArgumentParser(description="Simulate Enigma machine.")
parser.add_argument('-output_file', default="result.txt",
                    help='file with result (default: %(default)s)', metavar="")
parser.add_argument('input_file', help="file with text to encrypt/decrypt")
args = parser.parse_args()
print(args)
rotor_1st = rotorI
rotor_2nd = rotorII
rotor_3rd = rotorIII
rotors = [rotor_1st,  rotor_2nd, rotor_3rd]
reflector = reflectorUKWB
plugboard = Plugboard(["QE", "WS", "AB", "ZV", "TF", "OX", "RH"])
enigma = Enigma(rotors, reflector, ("D", "O", "N"), ("E", "G", "C"), plugboard)
result = ""

with open(args.input_file, "r") as file_handle:
    for line in file_handle:
        for letter in line:
            result += enigma.code_letter(letter)

with open(args.output_file, "w") as file_handle:
    file_handle.write(result)

# list = []
# while True:
    # letter = input("Give letter to encrypt: ")
    # list.append(enigma.code_letter(letter))
    # print(list)