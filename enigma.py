from rsc_manager import ResourcesManager
from enigma_gui.gui import gui_main
import argparse
import os


def main():
    cwd = os.getcwd()  # get working directory
    rsc_path = f"{cwd}/rsc"
    rsc = ResourcesManager(rsc_path)
    parser = argparse.ArgumentParser(description="Simulate Enigma machine.")

    parser.add_argument('-m', '--mode', default="gui",
                        help='define the mode in wich programme should be run\
                        [gui/cmd] (default: %(default)s)',
                        choices=["gui", "cmd"],
                        metavar="")
    parser.add_argument('-i', '--input_file', default=None,
                        help='file with plain text to encode, required\
                        in cmd mode', metavar="")
    parser.add_argument('-o', '--output_file', default="result.txt",
                        help='file with result (default: %(default)s)',
                        metavar="")
    parser.add_argument('-c', '--config',
                        default=f"{rsc_path}/config.json",
                        help='json file with initial configuration of machine\
                        (default: %(default)s)', metavar="")

    args = parser.parse_args()
    mode = args.mode
    if mode == "cmd":
        enigma = rsc.initailze_enigma_with_file(args.config)
        enigma.code_file(args.input_file, args.output_file)
    elif mode == "gui":
        gui_main(args)


if __name__ == "__main__":
    main()
