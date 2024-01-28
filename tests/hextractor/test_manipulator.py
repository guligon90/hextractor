from typing import List

import pytest

from hextractor.manipulator import StringManipulator


@pytest.mark.parametrize("str_value, expected_codes", [
    ("what ever", [119, 104, 97, 116, 32, 101, 118, 101, 114,]),
    ("CitricSheep", [67, 105, 116, 114, 105, 99, 83, 104, 101, 101, 112])
])
def test_extract_ascii_codes(str_value: str, expected_codes: List[int]):
    manipulator = StringManipulator(str_value)
    manipulator.extract_ascii_codes()
    
    assert manipulator.ascii_codes == expected_codes
