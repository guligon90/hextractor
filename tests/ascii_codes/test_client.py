from ascii_codes.client import extract_ascii_codes


def test_extract_ascii_codes_failure_invalid_input_type():
    response = extract_ascii_codes(12345)

    assert response.errors != None
    assert isinstance(response.errors, list)
    assert len(response.errors) == 1
    assert response.errors[0] == "A string must be informed in order to construct the payload"
