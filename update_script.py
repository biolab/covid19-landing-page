import requests
import json
import sys

r = requests.get(sys.argv[1], headers={'Authorization': sys.argv[2]})
r.raise_for_status()


payload = json.loads(r.text)

# Sanity check
if 'povabljeniPrebivalci' not in payload:
    raise ValueError

if 'sprejetaPovabila' not in payload:
    raise ValueError

if 'odvzetihVzorcev' not in payload:
    raise ValueError

if 'dateHour' not in payload:
    raise ValueError

with open('data/podatki.json', 'w') as fp:
    json.dump(payload, fp)
