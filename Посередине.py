with open('in_file.txt') as inlet, open('out_file.txt', 'w') as outlet:
    n = int(inlet.readline())
    data = list(map(str.strip, inlet.readlines()))
    average = sum([len(i) for i in data]) // len(data)
    outlet.write(str(average) + '\n')
    for i in data:
        if abs(len(i) - average) <= n:
            outlet.write(i + '\n')
