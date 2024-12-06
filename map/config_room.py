import json
import os

class Adapter:
    @staticmethod
    def adapt(path=None):
        
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'config.json')
        with open(path, "r") as rfile:
            data = json.load(rfile)
        return data["options"]



