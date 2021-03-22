import csv
import json

with open('dragons.csv') as inlet, open('dragons.json', 'w', encoding='utf-8') as outlet:
    reader = csv.DictReader(inlet, delimiter=',', quoting=csv.QUOTE_NONE)
    headers = reader.fieldnames
    answer = {'dragons': list()}
    for row in reader:
        answer['dragons'].append(dict())
        for i in headers:
            answer['dragons'][-1][i] = row[i]
    json.dump(answer, outlet, indent=4)
