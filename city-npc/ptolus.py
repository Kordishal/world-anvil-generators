import json
from typing import Any

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def create_payload_dict(variable: str):
    router = dict()
    router[variable] = dict()
    return router, router[variable]


def read_table_generators(items, payload):
    for item in items:
        key = item[0].value
        if key is None:
            continue
        if len(item) == 2:
            key = key.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '')
            payload[key] = {
                'value': item[0].value,
                'weight': int(item[1].value)
            }
        elif len(item) == 3:
            payload[item[0].value] = {
                'value': item[1].value,
                'weight': int(item[2].value)
            }


def read_table_routers(items, payload):
    for item in items:
        payload[item[0].value] = item[1].value


def read_range(sheet_range: str, filename: str, sheet):
    resource = filename.split('-')[-1] + 's'
    mortal = sheet[sheet_range]
    mortal_generator, mortal_payload = create_payload_dict('values')
    if resource == 'generators':
        read_table_generators(mortal, mortal_payload)
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
    read_range('D22:E25', 'less-than-mortal-generator', start)
    read_range('G5:H6', 'world-generator', start)
    read_range('J5:K6', 'gender-generator', start)

    read_range('B5:D7', 'city-demographics-generator', origin)
    read_range('B11:D13', 'down-shadow-demographics-generator', origin)
    read_range('F5:H8', 'major-race-generator', origin)
    read_range('F14:H27', 'minor-race-generator', origin)
    read_range('F36:H58', 'monstrous-race-generator', origin)
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
    read_range('N5:P9', 'power-type-generator', role)
    read_range('R5:S10', 'martial-class-generator', role)
    read_range('U5:V9', 'arcane-class-generator', role)
    read_range('X5:Y6', 'divine-class-generator', role)
    read_range('AA5:AB6', 'primal-class-generator', role)
    read_range('AD5:AE5', 'psi-class-generator', role)
    read_range('AG5:AH95', 'profession-generator', role)

    read_range('J5:K11', 'domain-death-generator', gods)
    read_range('M5:N11', 'domain-knowledge-generator', gods)
    read_range('P5:Q11', 'domain-life-generator', gods)
    read_range('G16:H22', 'domain-light-generator', gods)
    read_range('J16:K22', 'domain-luck-generator', gods)
    read_range('M16:N22', 'domain-nature-generator', gods)
    read_range('P16:Q22', 'domain-protection-generator', gods)
    read_range('G27:H33', 'domain-technology-generator', gods)
    read_range('J27:K33', 'domain-tempest-generator', gods)
    read_range('M27:N33', 'domain-trickery-generator', gods)
    read_range('P27:Q33', 'domain-war-generator', gods)

    read_range('B4:D22', 'domain-name-generator', gods)
    read_range('B27:C45', 'deity-name-router', gods)

