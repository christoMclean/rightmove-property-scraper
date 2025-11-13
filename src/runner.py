thonpython
import json
import logging
from pathlib import Path

from extractors.rightmove_parser import RightmoveParser
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO)

def main():
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "inputs.sample.json"
    output_path = base_dir / "data" / "sample_output.json"

    if not input_path.exists():
        logging.error(f"Input file not found: {input_path}")
        return

    with open(input_path, "r") as f:
        listings = json.load(f)

    parser = RightmoveParser()

    parsed_results = []
    for listing in listings:
        try:
            parsed = parser.parse_listing(listing)
            parsed_results.append(parsed)
        except Exception as e:
            logging.error(f"Failed to parse listing: {e}")

    exporter = JSONExporter()
    exporter.export(parsed_results, output_path)

    logging.info(f"Scraping complete. Output saved to {output_path}")

if __name__ == "__main__":
    main()