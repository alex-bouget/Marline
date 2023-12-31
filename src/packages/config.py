import json
from typing import Any
import os


class Config(dict[str, Any]):
    file: str

    def __init__(self, config_file: str) -> None:
        self.file = config_file
        # create directory if not exists
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        if os.path.exists(config_file):
            super().__init__(json.load(open(config_file)))
        else:
            super().__init__()
        self.save()

    def save(self) -> None:
        with open(self.file, "w") as f:
            f.write(json.dumps(self, indent=4))
