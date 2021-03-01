def genome(first, second):
    comp = 0
    for i, f in enumerate(first):
        if f == 'A' and second[i] == 'T' or f == 'T' and second[i] == 'A':
            comp += 1
        elif f == 'C' and second[i] == 'G' or f == 'G' and second[i] == 'C':
            comp += 1
    if len(first) - comp < len(first) * 3 / 10:
        return comp, True
    return comp, False
