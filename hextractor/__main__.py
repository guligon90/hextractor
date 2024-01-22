from __future__ import annotations
from typing import Optional

from .arguments import build_arguments_parser
from .manipulator import StringManipulator


def main(str_value: str, debug: Optional[bool] = False) -> str:
    """As per requested in: https://shorturl.at/ilsK0
    1. Start with the string "CitricSheep".
    2. Use the ASCII values of each character in the string and generate a list of these values.
    3. Multiply each value in the list by the number of characters in the string.
    4. Find the sum of all numbers in the resulting list.
    5. Use this sum to generate a SHA256 hash.
    6. Convert this hash to a hexadecimal string.
    """
    manipulator = StringManipulator(str_value) \
        .extract_ascii_codes(debug=debug) \
        .weigh_ascii_codes(debug=debug) \
        .sum_ascii_codes(debug=debug) \
        .build_hex_string(debug=debug)

    return manipulator.hex_string


if __name__ == "__main__":
    try:
        args_parser = build_arguments_parser()
        args = args_parser.parse_args()
        hex_string = main(args.value, args.debug)

        if not args.debug:
            print(f"\nHex string from {args.value}: {hex_string}")

    except KeyboardInterrupt:
        raise SystemExit("Program interrupted. Exiting...")
    except Exception as exc:
        raise SystemExit(f"{exc.__class__.__name__}: {str(exc)}")
