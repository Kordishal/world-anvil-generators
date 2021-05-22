import json

if __name__ == '__main__':

    with open('input.csv', 'r') as fp:
        values = dict()
        values['values'] = dict()
        for line in fp:
            name = line.strip()
            values['values'][name] = name

    with open('output.json', 'w') as fp:
        json.dump(values, fp, ensure_ascii=False, indent='    ')