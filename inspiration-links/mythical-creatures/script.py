import csv
import json

name_generator = dict()
name_generator['values'] = dict()

if __name__ == '__main__':
    with open('mythical-creatures-with-en-description.csv', 'r') as fp:
        reader = csv.reader(fp, dialect='unix')
        count = 0
        for row in reader:
            name_generator['values'][f'value{count}'] = {
                "value": f'[url:{row[0]}|tab]{row[1]}[/url], {row[2]}',
                "weight": 10
            }
            count += 1

    with open('mythical-creatures-generator.json', 'w') as fp:
        json.dump(name_generator, fp, ensure_ascii=False, indent='    ')
