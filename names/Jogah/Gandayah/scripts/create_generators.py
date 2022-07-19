import json

if __name__ == '__main__':

    files = {
        'crops.txt': 10,
        'insects.txt': 10,
        'plant-parts.txt': 20,
        'adirondack-plants.txt': 100,
        'positive-mood-or-emotion.txt': 5,
        'tool.txt': 5
    }
    combined_generator = dict()

    for f in files:
        with open(f'../sources/{f}', 'r') as fp:
            data = dict()

            for line in fp:
                line = line.strip()
                data[line] = line

            values = dict()
            values['values'] = data
            file = f.replace(".txt", "")
            with open(f'../generators/generator-{file}.json', 'w') as out:
                json.dump(values, out, ensure_ascii=False, indent='    ')

            combined_generator[file] = {
                'value': f'[generator:{file}-soullink|' + '{}' + f'|{file}-soullink_1]',
                'weight': files[f]
            }

    result_values = dict()
    result_values['values'] = combined_generator
    with open('../generators/gandayah-names.json', 'w') as fp:
        json.dump(result_values, fp, ensure_ascii=False, indent='    ')