import csv
import json
from typing import Any


def write_file(data: Any, filename: str):
    with open(f'{filename}.json', 'w') as fp:
        json.dump(data, fp, ensure_ascii=False, indent='    ')


if __name__ == '__main__':

    with open('new-article-links.csv', 'r') as fp:
        reader = csv.reader(fp, dialect='unix')
        router = dict()
        router['new-article-link'] = dict()
        for row in reader:
            router['new-article-link'][row[0]] = row[1]

    write_file(router, 'new-article-link-transformer')
