import json


class Adapter:
    @staticmethod
    def adapt(path="config.json"):
        with open(path, "r") as rfile:
            data = json.load(rfile)
        return data["settings"]



