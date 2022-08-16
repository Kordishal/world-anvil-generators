import json

if __name__ == '__main__':
    output = dict()
    values = dict()
    output['values'] = values
    with open('neighbourhoods.txt', 'r') as fp:
        for line in fp.readlines():
            line = line.strip()
            values[line] = f'[var:manhattan-{line}]'
    with open('neighbourhoods.json', 'w') as fp:
        json.dump(output, fp, ensure_ascii=False, indent='    ')
