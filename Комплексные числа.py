import json
import sys

inlet = list(map(str.strip, sys.stdin))
data = {'complex': list()}
for i in inlet:
    i = i.split()
    im = float(i[4])
    if i[3] == '-':
        im = -im
    data['complex'].append({'Re': float(i[2]), 'Im': im})

with open('output.json', 'w') as outlet:
    json.dump(data, outlet, indent=4)
