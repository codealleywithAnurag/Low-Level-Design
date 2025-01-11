class PrototypeManager:
    def __init__(self):
        self._prototypes = {}

    def addPrototype(self, key, prototype):
        self._prototypes[key] = prototype

    def getPrototype(self, key):
        if key in self._prototypes:
            return self._prototypes[key].clone()
        raise KeyError(f"No prototype found for key: {key}")
