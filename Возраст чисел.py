import json
import sys

data = [[] for _ in range(11)]
answer = dict()
with open('numbers_age.json', 'w', encoding='utf-8') as outlet:
    inlet = list(map(lambda x: int(x.strip()), sys.stdin))
    for number in inlet:
        if number < 10:
            data[1].append(str(number))
        else:
            n = number
            i = 0
            while n > 9:
                composition = 1
                for numeral in list(str(n)):
                    composition *= int(numeral)
                n = composition
                i += 1
            data[i].append(str(number))
    for i in range(len(data)):
        if data[i]:
            answer[str(i)] = data[i]
    json.dump(answer, outlet, indent=4)
