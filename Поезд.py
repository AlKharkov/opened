class Wagon:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'№{self.number}'

    def get_number(self):
        return self.number


class Train:
    def __init__(self, number, wagons=[]):
        self.number = number
        self.wagons = wagons

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        return f'Train {self.number}, {len(self.wagons)} вагонов'

    def __getitem__(self, item):
        return self.wagons[item]

    def __setitem__(self, key, value):
        self.wagons[key] = value

    def __delitem__(self, key):
        if key == -1 or key == len(self.wagons) - 1:
            self.wagons.pop()

    def __iter__(self):
        return iter(self.wagons)

    def get_number(self):
        return self.number

    def get_wagons(self):
        return self.wagons

    def append(self, wagon):
        self.wagons.append(wagon)
