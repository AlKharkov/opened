def vaccine_filter(n):
    d = []
    for i in immunoglobulins:
        if not n(i):
            d.append(i)
    for i in d:
        immunoglobulins.remove(i)
