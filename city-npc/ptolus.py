import json
from typing import Any

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

origin_keys = list()


def create_payload_dict(variable: str):
    router = dict()
    router[variable] = dict()
    return router, router[variable]


def read_table_generators(items, payload, is_origin):
    for item in items:
        key = item[0].value
        if key is None:
            continue
        if len(item) == 2:
            key = key.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '').replace("'", '')
            value = item[0].value
            payload[key] = {
                'value': value,
                'weight': int(item[1].value)
            }
            if is_origin and not value.startswith('['):
                origin_keys.append(key)
        elif len(item) == 3:
            key = item[0].value
            value = item[1].value
            payload[key] = {
                'value': value,
                'weight': int(item[2].value)
            }
            if is_origin and not value.startswith('['):
                origin_keys.append(key)


def read_table_routers(items, payload):
    for item in items:
        payload[item[0].value] = item[1].value


def read_range(sheet_range: str, filename: str, sheet):
    resource = filename.split('-')[-1] + 's'
    mortal = sheet[sheet_range]
    mortal_generator, mortal_payload = create_payload_dict('values')
    if resource == 'generators':
        read_table_generators(mortal, mortal_payload, sheet.title == 'ORIGIN')
    elif resource == 'routers':
        read_table_routers(mortal, mortal_payload)
    write_file(mortal_generator, filename, sheet.title.lower(), resource)


def write_file(data: Any, filename: str, folder: str, resource: str):
    with open(f'{folder}/{resource}/{filename}.json', 'w') as fp:
        json.dump(data, fp, ensure_ascii=False, indent='    ')


if __name__ == '__main__':

    wb = openpyxl.open('Ptolus_City_NPC_Encounter.xlsx')
    start: Worksheet = wb['START']
    origin = wb['ORIGIN']
    trait = wb['TRAITS']
    role = wb['ROLE']
    gods = wb['GODS']

    read_range('A5:B7', 'mortal-generator', start)
    read_range('D5:E16', 'more-than-mortal-generator', start)
    read_range('G5:H8', 'less-than-mortal-generator', start)
    read_range('J5:K7', 'mortality-router', start)
    read_range('M5:N7', 'world-generator', start)
    read_range('P5:Q6', 'gender-generator', start)

    read_range('B5:D7', 'city-demographics-generator', origin)
    read_range('B11:D13', 'down-shadow-demographics-generator', origin)
    read_range('F5:H8', 'major-race-generator', origin)
    read_range('F14:H27', 'minor-race-generator', origin)
    read_range('G36:H58', 'monstrous-race-generator', origin)
    read_range('J5:K7', 'aasimar-subrace-generator', origin)
    read_range('J11:K26', 'dragonborn-subrace-generator', origin)
    read_range('J30:K33', 'genasi-subrace-generator', origin)
    read_range('J37:K45', 'dwarven-subrace-generator', origin)
    read_range('J49:K59', 'elven-subrace-generator', origin)
    read_range('J63:K65', 'gnome-subrace-generator', origin)
    read_range('J69:K72', 'halfling-subrace-generator', origin)
    read_range('J76:K81', 'half-elf-subrace-generator', origin)
    read_range('J85:K89', 'tiefling-subrace-generator', origin)
    read_range('M5:N11', 'human-culture-generator', origin)

    print(origin_keys)
    with open('origin/origin-keys.csv', 'w') as ok:
        for key in sorted(origin_keys):
            ok.write(key + '\n')

    read_range('P4:Q103', 'origin-template-router', origin)

    read_range('A5:C8', 'role-generator', role)
    read_range('E5:F6', 'balance-or-specialist-generator', role)
    read_range('H5:I6', 'active-role-one-generator', role)
    read_range('H9:I10', 'active-role-two-generator', role)
    read_range('H13:I14', 'active-role-three-generator', role)
    read_range('H17:I18', 'active-role-four-generator', role)
    read_range('J5:L6', 'class-or-profession-role-one-generator', role)
    read_range('J9:L10', 'class-or-profession-role-two-generator', role)
    read_range('J13:L14', 'class-or-profession-role-three-generator', role)
    read_range('J17:L18', 'class-or-profession-role-four-generator', role)
    read_range('N5:P9', 'power-type-role-one-generator', role)
    read_range('N11:P15', 'power-type-role-two-generator', role)
    read_range('N17:P21', 'power-type-role-three-generator', role)
    read_range('N23:P27', 'power-type-role-four-generator', role)
    read_range('R5:S20', 'martial-class-generator', role)
    read_range('U5:V20', 'arcane-class-generator', role)
    read_range('X5:Y20', 'divine-class-generator', role)
    read_range('AA5:AB20', 'primal-class-generator', role)
    read_range('AD5:AE20', 'psi-class-generator', role)
    read_range('AG5:AH95', 'profession-generator', role)

    read_range('B4:D25', 'domain-name-generator', gods)

    read_range('G5:H20', 'domain-civilization-generator', gods)
    read_range('J5:K20', 'domain-death-generator', gods)
    read_range('M5:N20', 'domain-future-generator', gods)
    read_range('P5:Q20', 'domain-knowledge-generator', gods)
    read_range('S5:T20', 'domain-life-generator', gods)
    read_range('V5:W20', 'domain-light-generator', gods)
    read_range('AB5:AC20', 'domain-nature-generator', gods)
    read_range('AN5:AO20', 'domain-technology-generator', gods)
    read_range('AQ5:AR20', 'domain-tempest-generator', gods)
    read_range('AT5:AU20', 'domain-trickery-generator', gods)
    read_range('AW5:AX20', 'domain-war-generator', gods)

    read_range('B30:C51', 'domain-name-router', gods)
