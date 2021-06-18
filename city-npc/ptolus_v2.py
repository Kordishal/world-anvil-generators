import json
import os
import re
from typing import Any, List

import csv

origin_keys = list()


def create_payload_dict(variable: str):
    router = dict()
    router[variable] = dict()
    return router, router[variable]


def read_table_generators(items):
    payload = dict()
    for item in items:
        local_key = item[0]
        local_key = local_key.strip()
        if local_key == '':
            continue
        if len(item) == 2:
            value = item[0]
            local_key = local_key.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '').replace("'", '')
            payload[local_key] = {
                'value': value,
                'weight': int(item[1])
            }
        elif len(item) == 3:
            local_key = item[0]
            value = item[1]
            local_key = local_key.lower()
            payload[local_key] = {
                'value': value,
                'weight': int(item[2])
            }
    return payload


def read_table_routers(items):
    payload = dict()
    for item in items:
        payload[item[0]] = item[1]
    return payload


def convert_file(input_lines, filename: str, folder: str):
    outer_payload = dict()
    resource = filename.split('-')[-1]
    if resource == 'generator':
        payload = read_table_generators(input_lines)
    elif resource == 'router':
        payload = read_table_routers(input_lines)
    else:
        print(filename)
        return
    outer_payload['values'] = payload
    write_file(outer_payload, filename, folder, resource + 's')


def write_file(data: Any, filename: str, folder: str, resource: str):
    with open(f'{folder}/{resource}/{filename}.json', 'w') as wr:
        json.dump(data, wr, ensure_ascii=False, indent='    ')


if __name__ == '__main__':

    for root, directories, files in os.walk('./'):
        if root.endswith('source'):
            for file in files:
                with open(f'{root}/{file}', 'r') as fp:
                    lines = csv.reader(fp, dialect='unix')

                    convert_file(lines, file.rstrip('.csv'), root.split('/')[1])