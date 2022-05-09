"""Constants for feeds and feed entries."""
from __future__ import annotations

CUSTOM_NAMESPACES = {
    "http://webservices.ingv.it/fdsnws/event/1": "ingv",
}

URL_DEFAULT = "https://webservices.ingv.it/fdsnws/event/1/query"
URL_PATTERN_RADIUS = (
    "https://webservices.ingv.it/fdsnws/event/1/query?lat={}&lon={}&maxradiuskm={}"
)
URL_PATTERN_MAGNITUDE = "https://webservices.ingv.it/fdsnws/event/1/query?minmag={}"
URL_PATTERN_RADIUS_MAGNITUDE = "https://webservices.ingv.it/fdsnws/event/1/query?lat={}&lon={}&maxradiuskm={}&minmag={}"

XML_TAG_INGV_ID_LOCATOR = "ingv:id_locator"
