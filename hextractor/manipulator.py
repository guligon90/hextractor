from __future__ import annotations
from typing import List, Optional
from hashlib import sha256


class StringManipulator:
    def __init__(self, str_value: str) -> None:
        
        if len(str_value) == 0:
            raise ValueError("The informed string must not be empty") 
        
        self.str_value = str_value
        self.ascii_codes: List[int] = []
        self.weighted_codes: List[int] = []
        self.sum_of_codes: int = 0
        self.hex_string: str = ""

    def extract_ascii_codes(self, debug: Optional[bool] = False) -> StringManipulator:
        """Obtain the ASCII code of each character from the input string."""
        self.ascii_codes = [ord(char) for char in self.str_value]
        
        if (debug):
            print(f"\nASCII codes: {','.join([str(code) for code in self.ascii_codes])}")

        return self
        
    def weigh_ascii_codes(self, weight: Optional[int] = None, debug: Optional[bool] = False) -> StringManipulator:
        """Weigths each ASCII code previously obtained by a integer weight, by default, the size of the input string."""
        weight = len(self.str_value) if weight == None else weight

        self.weighted_codes = [weight * code for code in self.ascii_codes]

        if (debug):
            print(f"\nWeighted ASCII codes: {','.join([str(wcode) for wcode in self.weighted_codes])}")

        return self
        
    def sum_ascii_codes(self, debug: Optional[bool] = False) -> StringManipulator:
        """Sum the elements of the weighted ASCII code list."""
        self.sum_of_codes = sum(self.weighted_codes)

        if (debug):
            print(f"\nSum of weighted ASCII codes: {str(self.sum_of_codes)}")

        return self

    def build_hex_string(self, debug: Optional[bool] = False, encoding_format: Optional[str] = "utf-8") -> StringManipulator:
        """Apply the SHA256 to the weighted sum to obtain a hash, then extracts the hexadecimal digest from the hash."""
        encrypter = sha256()
        encrypter.update(str(self.sum_of_codes).encode(encoding_format))

        self.hex_string = encrypter.hexdigest()

        if debug:
            print(f"\nHex string from SHA256 hash: {self.hex_string}")
        
        return self
