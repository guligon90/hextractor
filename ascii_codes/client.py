from typing import Optional, Dict

from bs4 import BeautifulSoup as bs
from requests import request, Response

from .exceptions import AsciiClientRequestException
from .models import AsciiCodes, AsciiClientResponse
from .settings import DEFINITIONS
from .utils import get_hex


http_settings = DEFINITIONS["http"]


def build_payload(text_to_send: str) -> Dict[str, str] | None:
    if not isinstance(text_to_send, str):
        raise TypeError("A string must be informed in order to construct the payload")

    return {
        http_settings["form_field"]: text_to_send
    }


def parse_html_response(response: Response) -> AsciiCodes | None:
    http_text = response.text
    soup = bs(http_text, "html.parser")
    table = soup.find("table")

    if table != None:
        table_rows = table.find_all("tr")
        headers = table_rows[0].find_all("td")

        decimal_codes = []
        hex_codes = []
        octal_codes = []

        for row in table_rows:
            for i, cell in enumerate(row.find_all('td')):
                base_label = headers[i].find("b").string

                base_switcher = {
                    "Dec": lambda v: decimal_codes.append(int(v)),
                    "Oct": lambda v: octal_codes.append(int(v)),
                    "Hex": lambda v: hex_codes.append(get_hex(v)[0])
                }

                if cell.string not in ["Dec", "Oct", "Hex"]:
                    base_list_callable = base_switcher.get(base_label)

                    if base_list_callable != None:
                        base_list_callable(cell.string)
        model = AsciiCodes(**{
            "decimal": decimal_codes,
            "hexadecimal": hex_codes,
            "octal": octal_codes,
        })

        return model


def make_request(payload: Dict[str, str], url: Optional[str] = http_settings["base_url"]) -> Response:
    headers = http_settings["headers"]
    method = http_settings["method"]
    response = request(method, url, headers=headers, data=payload, files=[])

    if (response.status_code != 200):
        raise AsciiClientRequestException(f"The request for extracting ASCII codes return with status {response.status_code}")

    return response


def extract_ascii_codes(text_to_send: str) -> AsciiClientResponse:
    model_payload = {
        "ascii_codes": None,
        "errors": None,
    }

    try:
        payload = build_payload(text_to_send)
        response = make_request(payload)
    
        ascii_codes = parse_html_response(response)
        model_payload.update({
            "ascii_codes": ascii_codes,
        })
    except TypeError as texc:
        model_payload.update({
            "errors": [str(texc), ],
        })
    except AsciiClientRequestException as rexc:
        model_payload.update({
            "errors": [str(rexc), ],
        })        
    finally:
        model = AsciiClientResponse(**model_payload)

        return model
