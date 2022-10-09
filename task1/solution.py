import json
import csv

with open('./data.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader)
    Ukraine = {'Ukraine': {'people': [], 'count': 0}}
    USA = {'USA': {'people': [], 'count': 0}}
    Paris = {'Paris': {'people': [], 'count': 0}}
    India = {'India': {'people': [], 'count': 0}}
    for row in reader:
        if row[0] == 'Ukraine':
            N = len(row[1])
            Ukraine['Ukraine']['people'].append(row[1])
            Ukraine['Ukraine']['count'] = len(Ukraine['Ukraine']['people'])
        elif row[0] == 'USA':
            N = len(row[1])
            USA['USA']['people'].append(row[1])
            USA['USA']['count'] = len(USA['USA']['people'])
        elif row[0] == 'Paris':
            N = len(row[1])
            Paris['Paris']['people'].append(row[1])
            Paris['Paris']['count'] = len(Paris['Paris']['people'])
        else:
            N = len(row[1])
            India['India']['people'].append(row[1])
            India['India']['count'] = len(India['India']['people'])

        with open('results.json', 'w') as f:
            json.dump((Ukraine, USA, Paris, India), f, indent=4)