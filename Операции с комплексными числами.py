import json

with open('in.json') as f:
    data = json.load(f)
    re1, re2 = data['complex'][0]['Re'], data['complex'][1]['Re']
    im1, im2 = data['complex'][0]['Im'], data['complex'][1]['Im']
data = {'complex': [{'Re': re1 + re2, 'Im': im1 + im2}, {'Re': re1 - re2, 'Im': im1 - im2},
                    {'Re': re1 * re2 - im1 * im2, 'Im': re1 * im2 + re2 * im1}]}

with open('out.json', 'w') as outlet:
    json.dump(data, outlet, indent=4)
