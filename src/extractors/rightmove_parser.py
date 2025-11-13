thonpython
import logging
from .geo_utils import extract_coordinates

class RightmoveParser:
    """Simple parser converting raw listing dicts into structured output"""

    def parse_listing(self, raw: dict) -> dict:
        logging.debug("Parsing listing...")

        listing = {
            "id": raw.get("id"),
            "propertyUrl": raw.get("url"),
            "summary": raw.get("summary", ""),
            "displayAddress": raw.get("address", ""),
            "bedrooms": raw.get("bedrooms", 0),
            "bathrooms": raw.get("bathrooms", 0),
            "price": {
                "amount": raw.get("price", {}).get("amount"),
                "currencyCode": raw.get("price", {}).get("currency"),
            },
            "propertyImages": {"images": raw.get("images", [])},
            "location": extract_coordinates(raw.get("map", {})),
            "channel": raw.get("channel", "UNKNOWN"),
        }

        return listing