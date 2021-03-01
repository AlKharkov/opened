def vaccine_filter(func):
    deleted = True
    while deleted:
        deleted = False
        for i in range(len(immunoglobulins)):
            if i >= len(immunoglobulins):
                break
            if not any(filter(func, [immunoglobulins[i]])):
                immunoglobulins.pop(i)
                deleted = True
