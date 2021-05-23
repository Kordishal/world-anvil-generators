import json

if __name__ == '__main__':

    with open('input.csv', 'r') as fp:
        values = dict()
        values['values'] = dict()
        value = 'value'
        count = 1
        for line in fp:
            name = line.strip()
            values['values'][f'{value}{count}'] = name
            count += 1
    with open('output.json', 'w') as fp:
        json.dump(values, fp, ensure_ascii=False, indent='    ')