with open('data.txt') as inlet:
    n = int(inlet.readline())
    A = set(map(lambda x: int(x), inlet.readline().split()))
    answer = 0
    for i in range(2, n):
        for j in A:
            if i % j == 0:
                answer += i
                break
    print(answer)
