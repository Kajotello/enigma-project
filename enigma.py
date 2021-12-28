from rsc_manager import ResourcesManager
import argparse
import os


def main():
    cwd = os.getcwd()  # get working directory
    rsc_path = f"{cwd}/rsc"
    rsc = ResourcesManager(rsc_path)
    parser = argparse.ArgumentParser(description="Simulate Enigma machine.")

    parser.add_argument('-output_file', default="result.txt",
                        help='file with result (default: %(default)s)',
                        metavar="")
    parser.add_argument('-configuration',
                        default=f"{rsc_path}/config.json",
                        help='json file with initial configuration of machine\
                        (default %(default)s)', metavar="")
    parser.add_argument('input_file', help="file with text to encrypt/decrypt")

    args = parser.parse_args()
    rsc.conf.get_temp_config_from_file(args.configuration)
    enigma = rsc.initialize_enigma()

    result = ""
    space_dist = 5

    with open(args.input_file, "r") as file_handle:
        for line in file_handle:
            for i, letter in enumerate(line):
                result += enigma.code_letter(letter)
                if i % space_dist == space_dist - 1:
                    result += " "

    with open(args.output_file, "w") as file_handle:
        file_handle.write(result)


if __name__ == "__main__":
    main()
