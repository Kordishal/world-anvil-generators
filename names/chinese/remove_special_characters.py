import re

if __name__ == '__main__':
    output = set()
    unique_with = set()
    with open('sources/wikidata-given-names.csv', 'r') as fp:
        for line in fp.readlines():
            line = line.strip()
            unique_with.add(line)
            line = re.sub('[éèěē]', 'e', line)
            line = re.sub('[ÉÈĚĒ]', 'E', line)
            line = re.sub('[īìíǐ]', 'i', line)
            line = re.sub('[ōǒóò]', 'o', line)
            line = re.sub('[àáāǎ]', 'a', line)
            line = re.sub('[ĀÀǍÁ]', 'A', line)
            line = re.sub('[ùúǔū]', 'u', line)
            output.add(line)

    output = sorted(output)
    unique_with = sorted(unique_with)

    # after regenerating this a sort with LibreOffice is required as it is lexical and not alphabetical ordering
    # with open('sources/wikidata-given-names.csv', 'w') as fp:
    #    for item in unique_with:
    #        fp.write(item + '\n')
    with open('sources/wikidata-given-names-no-diacritics.csv', 'w') as fp:
        for item in output:
            fp.write(item + '\n')