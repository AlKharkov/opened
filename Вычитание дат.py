class Date:
    def __init__(self, month, day):
        calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.month = month
        self.day = day
        count = day
        for i in range(month - 1):
            count += calendar[i]
        self.count = count

    def __sub__(self, other):
        return self.count - other.count
