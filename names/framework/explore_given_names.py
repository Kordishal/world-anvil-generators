import json
import os
import re

values = dict()
values['female'] = dict()
values['male'] = dict()
values['unisex'] = dict()
values['other'] = dict()

surnames_dict = dict()

given_name_categories = set()
surname_categories = set()
if __name__ == '__main__':
    with open('kaikki.org-dictionary-all.json', 'r') as fp:
        for line in fp.readlines():
            word = dict()
            line = line.strip()
            data = json.loads(line)
            word['pos'] = data['pos']
            if word['pos'] != 'name':
                continue
            word['word'] = data['word']
            word['lang'] = data['lang']
            word['lang_code'] = data['lang_code']
            for item in data['senses']:
                if 'categories' in item:
                    cat = [i['name'] for i in item['categories']]
                    word['categories'] = cat

            if 'categories' in word and len(word['categories']) > 0:
                for category in word['categories']:
                    if 'given names' in category:
                        given_name_categories.add(category)
                        if ' male' in category:
                            if category in values['male']:
                                values['male'][category].append(word['word'])
                            else:
                                values['male'][category] = [word['word']]
                        elif 'female' in category:
                            if category in values['female']:
                                values['female'][category].append(word['word'])
                            else:
                                values['female'][category] = [word['word']]
                        elif 'unisex' in category:
                            if category in values['unisex']:
                                values['unisex'][category].append(word['word'])
                            else:
                                values['unisex'][category] = [word['word']]
                        else:
                            if category in values['other']:
                                values['other'][category].append(word['word'])
                            else:
                                values['other'][category] = [word['word']]
                    elif 'surnames' in category:
                        surname_categories.add(category)
                        if category in surnames_dict:
                            surnames_dict[category].append(word['word'])
                        else:
                            surnames_dict[category] = [word['word']]

with open('given_name_categories.json', 'w') as fp:
    json.dump(sorted(list(given_name_categories)), fp, ensure_ascii=False, indent='    ')
with open('surname_categories.json', 'w') as fp:
    json.dump(sorted(list(surname_categories)), fp, ensure_ascii=False, indent='    ')


if not os.path.exists('output/generators/given-names'):
    os.mkdir('output/generators/given-names')

for folder in ['male', 'female', 'unisex', 'other']:
    if not os.path.exists(f'output/generators/given-names/{folder}'):
        os.mkdir(f'output/generators/given-names/{folder}')

if not os.path.exists('output/generators/surnames'):
    os.mkdir('output/generators/surnames')

for key in values:
    for category in values[key]:
        words = values[key][category]
        if len(words) <= 10:
            continue
        if not re.match(r'^[A-Z]', words[0]):
            continue
        count = 0
        generator = dict()
        generator['values'] = dict()
        for word in words:
            generator['values'][f'value{count}'] = word
            count += 1
        with open(f'output/generators/given-names/{key}/{category}.json', 'w') as fp:
            json.dump(generator, fp, ensure_ascii=False, indent='    ')

for key in surnames_dict:
    words = surnames_dict[key]
    if len(words) <= 10:
        continue
    if not re.match(r'^[A-Z]', words[0]):
        continue
    count = 0
    generator = dict()
    generator['values'] = dict()
    for word in words:
        generator['values'][f'value{count}'] = word
        count += 1
    with open(f'output/generators/surnames/{key}.json', 'w') as fp:
        json.dump(generator, fp, ensure_ascii=False, indent='    ')