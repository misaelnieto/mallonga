#!/usr/bin/env python3
import csv
import string
import random
import json

def random_hash():
    """
    TODO: This is just a placeholder function. We will remove it later
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=8))

data = []
with open('links.csv') as csvfile:
    print('Importing csv ...')
    reader = csv.reader(csvfile)
    pk=0
    for row in reader:
        pk+=1
        data.append({
            "model": "shortener.urlmodel",
            "pk": pk,
            "fields": {
                "code": random_hash(),
                "url": row[0],
                "title": row[1],
                "cover": "",
                "hits": row[2],
                "created": "2020-03-29T07:13:36.746Z",
                "updated": "2020-03-29T07:13:36.746Z"
            }
        })

with open('links.json', 'w') as jsonfile:
    print('Exporting to json ...')
    jsonfile.write(json.dumps(data))

print ('Done.')