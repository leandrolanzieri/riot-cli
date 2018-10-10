import yaml

class RiotConfig():
    @staticmethod
    def parse_config(path=''):
        with open(path) as f:
            text = f.read()
        return yaml.load(text)
