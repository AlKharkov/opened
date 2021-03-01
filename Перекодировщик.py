with open('cyrillic.txt', encoding='utf-8') as in_file, open('transliteration.txt', 'w',
                                                             encoding='utf-8') as out_file:
    data = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
            "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
            "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
            "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
            "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
            "б": "b", "ю": "ju", "ё": "jo"}
    inlet = in_file.read()
    for i in inlet:
        if i in data.keys():
            out_file.write(data[i])
        elif i.lower() in data.keys():
            out_file.write(data[i.lower()].capitalize())
        else:
            out_file.write(i)
