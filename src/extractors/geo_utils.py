thonpython
def extract_coordinates(map_info: dict) -> dict:
    """Extract lat/lon safely."""
    lat = map_info.get("lat")
    lon = map_info.get("lng")

    if lat is None or lon is None:
        return {"latitude": None, "longitude": None}

    return {"latitude": lat, "longitude": lon}