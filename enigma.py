from rsc_manager import ResourcesManager
import argparse
import os


def main():
    cwd = os.getcwd()  # get working directory
    rsc_path = f"{cwd}/rsc"
    rsc = ResourcesManager(rsc_path)
    parser = argparse.ArgumentParser(description="Simulate Enigma machine.")

    parser.add_argument('--cmd', default="result.txt",
                        help='use programme in command line',
                        metavar="")
    parser.add_argument('--gui', default="result.txt",
                        help='use programme with GUI',
                        metavar="")
    parser.add_argument('--input_file',
                        help='file with plain text to encode, required\
                        with --cmd flag', metavar="")
    parser.add_argument('--output_file', default="result.txt",
                        help='file with result (default: %(default)s)',
                        metavar="")
    parser.add_argument('--configuration',
                        default=f"{rsc_path}/config.json",
                        help='json file with initial configuration of machine\
                        (default %(default)s)', metavar="")

    args = parser.parse_args()
    rsc.conf.get_temp_config_from_file(args.configuration)
    enigma = rsc.initialize_enigma()
    enigma.code_file(args.input, args.output)


if __name__ == "__main__":
    main()
