import sys

n = int(input())
data = list(map(str.strip, sys.stdin))
for i in data:
    a = n % len(i)
    if a > 0:
        print(i[a:] + i[:a])
    else:
        print(i[-a:] + i[:-a])
