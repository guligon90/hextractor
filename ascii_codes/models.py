from typing import List

from pydantic import BaseModel


class AsciiCodes(BaseModel):
    decimal: List[int]
    hexadecimal: List[str]
    octal: List[int]

    class ConfigDict:
        extra = "forbid"


class AsciiClientResponse(BaseModel):
    ascii_codes: AsciiCodes | None
    errors: List[str] | None

    class ConfigDict:
        extra = "forbid"
