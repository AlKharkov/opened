import json

answer = dict()
with open('russian_words.txt', encoding='utf-8') as inlet, open('russian_words.json', 'w',
                                                                encoding='utf-8') as outlet:
    for i in map(str.strip, inlet.readlines()):
        if i[0] not in answer.keys():
            answer[i[0]] = [i]
        else:
            answer[i[0]].append(i)
    json.dump(answer, outlet, indent=4, ensure_ascii=False)
