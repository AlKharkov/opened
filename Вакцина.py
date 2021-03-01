def vaccine_effect(value):
    deleted = True
    while deleted:
        deleted = False
        for i in range(len(immunoglobulins)):
            if i >= len(immunoglobulins):
                break
            if immunoglobulins[i][1] < value:
                immunoglobulins.pop(i)
                deleted = True
