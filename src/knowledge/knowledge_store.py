import json
from pathlib import Path


class KnowledgeStore:

    def __init__(self):

        self.file = Path("knowledge.json")

    def save(self, knowledge):

        with open(self.file, "w") as f:

            json.dump(
                knowledge,
                f,
                indent=4
            )

    def load(self):

        if not self.file.exists():

            return None

        with open(self.file) as f:

            return json.load(f)