class FastFibonacci:
    def __init__(self):
        self.numbers = {0: 1, 1: 1}

    def __call__(self, number):
        number -= 1
        dict_keys = list(self.numbers.keys())
        index = -1
        for i in range(len(dict_keys)):
            if dict_keys[i] == number:
                return self.numbers[number]
            if dict_keys[i] > number:
                index = i - 1
                break
        index = self.numbers[dict_keys[index]]
        while index != number:
            self.numbers[index + 1] = self.numbers[index] + self.numbers[index - 1]
            index += 1
        return self.numbers[number]
