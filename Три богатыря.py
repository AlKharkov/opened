from functools import total_ordering


@total_ordering
class EpicHero:
    def __init__(self, name, count_win, weapons):
        self.name = name
        self.count = count_win
        self.weapons = weapons

    def __str__(self):
        return f'Epic Hero {self.name}, {self.count}'

    def __repr__(self):
        return f"EpicHero('{self.name}', {self.count}, {sorted(self.weapons)})"

    def __eq__(self, other):
        return (len(self.name), self.count, len(self.weapons)) == \
               (len(other.name), other.count, len(other.weapons))

    def __gt__(self, other):
        return (self.count, len(self.weapons), -len(self.name), self.name) > \
               (other.count, len(other.weapons), -len(other.name), other.name)

    def add_win(self):
        self.count += 1

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def del_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
