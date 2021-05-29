class MinStat:
    def __init__(self):
        self.minimal = 1.5

    def add_number(self, number):
        if number < self.minimal or self.minimal == 1.5:
            self.minimal = number

    def result(self):
        return None if self.minimal == 1.5 else self.minimal


class MaxStat:
    def __init__(self):
        self.maximal = 1.5

    def add_number(self, number):
        if number > self.maximal or self.maximal == 1.5:
            self.maximal = number

    def result(self):
        return None if self.maximal == 1.5 else self.maximal


class AverageStat:
    def __init__(self):
        self.sum = 0
        self.count = 0

    def add_number(self, number):
        self.sum += number
        self.count += 1

    def result(self):
        return None if self.count == 0 else self.sum / self.count
