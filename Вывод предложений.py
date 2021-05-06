class LeftParagraph:
    def __init__(self, number):
        self.base = ''
        self.number = number

    def add_word(self, word):
        if not self.base:
            self.base = word
        elif len(self.base + ' ' + word) > self.number:
            print(self.base)
            self.base = word
        else:
            self.base += ' ' + word

    def end(self):
        self.base = ''
        if self.base:
            print(self.base)


class RightParagraph:
    def __init__(self, number):
        self.base, self.number = '', number

    def add_word(self, word):
        if not self.base:
            self.base = word
        elif len(self.base + ' ' + word) > self.number:
            print(' ' * (self.number - len(self.base)) + self.base)
            self.base = word
        else:
            self.base += ' ' + word

    def end(self):
        self.base = ''
        if self.base:
            print(' ' * (self.number - len(self.base)) + self.base)
