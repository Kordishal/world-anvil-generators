import csv
import json
import os

if __name__ == '__main__':

    with open('article-template-core.csv', 'r') as source:
        source_data = csv.reader(source)

        source_dict = dict()
        for item in source_data:
            source_dict[item[0]] = {
                'name': item[1],
                'link': item[2],
                'intro': item[3],
                'connector': item[4]
            }

    master = dict()
    master['values'] = dict()
    inner = master['values']

    with open('relationships-source-file.csv', 'r') as fp:
        reader = csv.reader(fp)

        for line in reader:
            directory = f'relationships/{line[0]}'
            with open(f'{directory}/{line[1]}.txt', 'r') as file:

                relations = [x.strip() for x in file.readlines()]

                values = dict()
                values['values'] = dict()
                for item in relations:
                    values['values'][item.replace(' ', '-')] = item

                with open(f'{directory}/{line[1]}.json', 'w') as jsonfile:
                    json.dump(values, jsonfile, ensure_ascii=False, indent='    ')

            key = f'{line[0]}-{line[1]}'
            source_items = source_dict[line[0]]
            braces = '{}'
            target = '{"target-article":"target-template-1"}'
            relation_key = key if line[2] == 'specific' else 'default'

            value = f'{source_items["intro"]} [url:{source_items["link"]}|tab]{source_items["name"]}[/url], ' \
                    f'{source_items["connector"]} [generator:prompt-relationships-{relation_key}-soullink|{braces}|relation] ' \
                    f'[generator:{line[1]}-article-28world29-soullink|{braces}|target] ({line[1]}).'

            inner[key] = {
                'value': value,
                'weight': line[3]
            }

    with open('master-generator.json', 'w') as file_master:
        json.dump(master, file_master, ensure_ascii=False, indent='    ')
