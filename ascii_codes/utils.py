from typing import Tuple


def get_hex(hex_repr: str) -> Tuple[int, str]:
    converted_string = int(hex_repr, base=16)
    converted_hex = hex(converted_string)
    
    return (converted_hex, converted_string)
