import sys

with open('output.txt', 'w') as inlet:
    data = list(map(lambda x: int(x.strip()), sys.stdin))
    writed = []
    for i in enumerate(data):
        if i[0] + 1 == i[1]:
            writed.append(str(i[1]))
    if writed:
        inlet.write(' '.join(map(lambda x: str(x), writed)))
    else:
        inlet.write('0')
