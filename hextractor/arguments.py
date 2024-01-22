from argparse import ArgumentParser

from .formatting import FormatText


def build_arguments_parser() -> ArgumentParser:
    main_parser = ArgumentParser(
        "hextractor",
        description=FormatText.bold("A program, written in Python 3.10.12, that obtains a hexadecimel string, from another string, "
        "through a steps involving extracting ASCII codes from the original string and applying  "
        "the SHA256 hashing algorithm")
    )

    main_parser.add_argument(
        "-v",
        "--value",
        type=str,
        required=True,
        default="CitricSheep",
        help=FormatText.bold("The string used to obain the hexadecimal string."),
    )

    main_parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        required=False,
        help=FormatText.bold("Flag to make the program print the result of each step"),
    )

    return main_parser
