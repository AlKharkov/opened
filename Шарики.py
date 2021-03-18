import json

with open('input.json') as inlet:
    print(*[i['id'] for i in
            sorted(json.load(inlet), key=lambda x: (len(x['colors']), x['radius'], x['x'] ** 2 + x['y'] ** 2, x['id']),
                   reverse=True)])
