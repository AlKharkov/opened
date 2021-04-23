class ModularArithmetic:
    def __init__(self, number, modular):
        self.number = number
        self.modular = modular

    def __call__(self, number):
        return number // self.modular

    def __add__(self, other):
        return ModularArithmetic(self.number + other.number, self.modular)

    def __sub__(self, other):
        return ModularArithmetic(self.number - other.number, self.modular)

    def __str__(self):
        while self.number < 0:
            self.number += self.modular
        while self.number >= self.modular:
            self.number -= self.modular
        return f'{self.number}({self.modular})'

    def __repr__(self):
        return str(self)

    def __rshift__(self, other):
        return ModularArithmetic(self.number + other, self.modular)

    def __lshift__(self, other):
        return ModularArithmetic(self.number - other, self.modular)
