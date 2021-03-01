def good_dreams(text, first_divisor, second_divisor, *args, **kwargs):
    text = text.split(first_divisor)
    for i in range(len(text)):
        text[i] = text[i].split(second_divisor)
    corteges = set()
    for i in args:
        corteges.add(i[0])
    name_funcs = set()
    for i in kwargs:
        name_funcs.add(i.split('=')[0])
    funcs = corteges & name_funcs
    for i in args:
        if i[0] in funcs:
            text[i[1]] = list(map(kwargs[i[0]], text[i[1]]))
    return text
