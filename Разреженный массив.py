class SparseArray:
    def __init__(self):
        self.array = dict()

    def __setitem__(self, key, value):
        self.array[key] = value

    def __getitem__(self, item):
        return self.array[item] if item in self.array.keys() else 0
