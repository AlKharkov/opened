s = 0
with open('prices.txt', mode='r') as f:
    for line in f:
        line = line.rstrip().split('\t')
        s += float(line[2]) * int(line[1])
print(f'{s:.2f}')
