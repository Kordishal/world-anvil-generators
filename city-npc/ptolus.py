import json
from typing import Any

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def create_payload_dict(variable: str):
    router = dict()
    router[variable] = dict()
    return router, router[variable]


def read_table(items, payload):
    for item in items:
        if len(item) == 2:
            payload[item[0].value.lower().replace(' ', '-').replace('(', '').replace(')', '')] = {
                'value': item[0].value,
                'weight': int(item[1].value)
            }
        elif len(item) == 3:
            payload[item[0].value] = {
                'value': item[1].value,
                'weight': int(item[2].value)
            }


def read_range(sheet_range: str, filename: str, sheet):
    mortal = sheet[sheet_range]
    mortal_generator, mortal_payload = create_payload_dict('values')
    read_table(mortal, mortal_payload)
    write_file(mortal_generator, filename, sheet.title.lower(), filename.split('-')[-1] + 's')


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

    read_range('A5:B7', 'city-demographics-generator', origin)
    read_range('A11:B13', 'down-shadow-demographics-generator', origin)
    read_range('D5:E8', 'major-race-generator', origin)
    read_range('D14:E27', 'minor-race-generator', origin)
    read_range('D36:E58', 'monstrous-race-generator', origin)
    read_range('G5:H7', 'aasimar-subrace-generator', origin)
    read_range('G11:H26', 'dragonborn-subrace-generator', origin)
    read_range('G30:H33', 'genasi-subrace-generator', origin)
    read_range('G37:H45', 'dwarven-subrace-generator', origin)
    read_range('G49:H59', 'elven-subrace-generator', origin)
    read_range('G63:H65', 'gnome-subrace-generator', origin)
    read_range('G69:H72', 'halfling-subrace-generator', origin)
    read_range('G76:H81', 'half-elf-subrace-generator', origin)
    read_range('G85:H89', 'tiefling-subrace-generator', origin)
    read_range('J5:K11', 'human-culture-generator', origin)

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

