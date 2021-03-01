with open('input.txt') as inlet, open('output.txt', 'w') as outlet:
    data = inlet.read().strip()
    nums = set('-0123456789')
    good_data = []
    s = ''
    for i in data:
        if i in nums:
            s += i
        else:
            good_data.append(float(s))
            s = ''
    try:
        good_data.append(float(s))
    except ValueError:
        pass
    ans = [[0, 1], [0, -1], [0, 0]]
    for i in good_data:
        if i > 0:
            ans[0][0] += 1
        elif i == 0:
            ans[2][0] += 1
        else:
            ans[1][0] += 1
    ans.sort(reverse=True)
    outlet.write(str(len(good_data)) + '\n')
    if ans[0][0] != 0:
        outlet.write(f'{ans[0][1]} {ans[0][0]}')
        if ans[1][0] != 0:
            outlet.write(f' {ans[1][1]} {ans[1][0]}')
            if ans[2][0] != 0:
                outlet.write(f' {ans[2][1]} {ans[2][0]}')
