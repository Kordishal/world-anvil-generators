import re

if __name__ == '__main__':
    output = list()
    with open('../sources/plants-adirondack.txt', 'r') as fp:

        for line in fp:
            values = line.split('\t')
            value = values[1]
            value = value.strip()
            if '(' in value:
                value = re.sub(r'\(.*\)', '', value)
                value = value.replace('  ', ' ')

            value = value.replace('American ', '')
            value = value.replace('Canada ', '')
            value = value.split('/')[0]
            if value.islower():
                output.append(value)

    with open('../sources/plants-adirondack-cleaned.txt', 'w') as fp:
        for i in output:
            fp.write(i + '\n')
