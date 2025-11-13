thonpython
import json
import logging
from pathlib import Path

class JSONExporter:
    def export(self, data, filepath: Path):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        logging.info(f"Exported {len(data)} records to {filepath}")