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
        if self.base:
            print(' ' * (self.number - len(self.base)) + self.base)


'''
lp = LeftParagraph(8)
lp.add_word('btdwmgil')
lp.add_word('sfwvgybz')
lp.add_word('fkq')
lp.add_word('dtovf')
lp.add_word('p')
lp.add_word('sqjulmv')
lp.add_word('erwao')
lp.add_word('kx')
lp.add_word('r')
lp.add_word('ehypl')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('btdwmgil')
rp.add_word('sfwvgybz')
rp.add_word('fkq')
rp.add_word('dtovf')
rp.add_word('p')
rp.add_word('sqjulmv')
rp.add_word('erwao')
rp.add_word('kx')
rp.add_word('r')
rp.add_word('ehypl')
rp.end()
print()
'''
