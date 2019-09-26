import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_codes']
with open('new_states.json', 'w') as g:
    json.dump(data, g, indent = 2)