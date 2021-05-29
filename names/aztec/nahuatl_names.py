import csv
import json
import random
from typing import List, Set


class MarkovChain:

    def __init__(self, data: List[str], order: int = 2, min_length: int = 4, max_length: int = 9):
        self.order = order
        self.min_length = min_length
        self.max_length = max_length

        self.start = list()
        self.database = dict()

        for word in data:
            if self.order > len(word):
                pass
            elif self.order == len(word):
                self.start.append(word)
            else:
                position = self.order
                part = word[0:position]
                self.start.append(part)
                next_part = word[position:position+self.order]
                while part:
                    if part not in self.database:
                        self.database[part] = [next_part]
                    else:
                        self.database[part].append(next_part)
                    position += self.order
                    part = next_part
                    next_part = word[position:position+self.order]

    def generate_word(self) -> str:
        current_part = random.choice(self.start)
        word = current_part
        repeat = 0
        while True:
            if repeat >= 10:
                return word
            try:
                next_part_options = self.database[current_part]
                unique_next_parts = set(next_part_options)
                if len(unique_next_parts) == 1 and '' in unique_next_parts and len(word) < self.min_length:
                    return word
                next_part = random.choice(next_part_options)
                if next_part == '':
                    if len(word) >= self.min_length:
                        return word
                else:
                    word += next_part
                    if len(word) >= self.max_length:
                        return word
                    current_part = next_part
            except KeyError:
                return word


def generate_names(items: Set[str], order: int, max_length: int):
    chain = MarkovChain(list(items), order=order, max_length=max_length)
    all_words = set()
    not_new_count = 0
    if order == 2:
        max_not_new_count = 1000
    elif order == 3:
        max_not_new_count = 10000
    elif order == 4:
        max_not_new_count = 100000
    else:
        max_not_new_count = 100
    while not_new_count < max_not_new_count:
        new_word = chain.generate_word()
        if new_word in all_words:
            not_new_count += 1
        else:
            not_new_count = 0
            all_words.add(new_word)
    print(f"Generated: Order {order}; Max Length {max_length}; Total {len(all_words)}")
    return all_words


def generate_name_list(items: Set[str], order: int):
    print(f"Total {order}: {len(items)}")
    generated_names = dict()
    generated_names['values'] = dict()
    for word in items:
        generated_names['values'][word.lower().replace(' ', '-')] = word
    with open(f'fantasy-name-generator-order-{order}.json', 'w') as fp:
        json.dump(generated_names, fp, ensure_ascii=False, indent='    ')


if __name__ == '__main__':
    names = set()

    values = dict()
    values['values'] = dict()
    inner = values['values']

    meaning_transformer = dict()
    meaning_transformer['meaning'] = dict()
    meaning_transformer_inner = meaning_transformer['meaning']

    gender_transformer = dict()
    gender_transformer['gender'] = dict()
    gender_transformer_inner = gender_transformer['gender']

    source_transformer = dict()
    source_transformer['source'] = dict()
    source_transformer_inner = source_transformer['source']

    with open('source.csv', 'r') as fp:
        reader = csv.reader(fp, dialect='unix')
        count = 1
        for row in reader:
            if count == 1:
                count += 1
                continue
            name = row[0].strip()
            meaning = row[1].strip()
            source_name = row[2].strip()
            gender = row[3].strip()
            source = row[4].strip()
            if name in names:
                print("Duplicate: " + name)
            else:
                names.add(name)
            key = name.lower().replace(' ', '-')
            inner[key] = name
            meaning_transformer_inner[key] = meaning
            gender_transformer_inner[key] = gender
            source_transformer_inner[key] = f'[url:{source}|tab]{source_name}[/url]'

    with open('all-names-generator.json', 'w') as fp:
        json.dump(values, fp, ensure_ascii=False, indent='    ')

    with open('router-names-to-meaning.json', 'w') as fp:
        json.dump(meaning_transformer, fp, ensure_ascii=False, indent='    ')

    with open('router-names-to-gender.json', 'w') as fp:
        json.dump(gender_transformer, fp, ensure_ascii=False, indent='    ')

    with open('router-names-to-source.json', 'w') as fp:
        json.dump(source_transformer, fp, ensure_ascii=False, indent='    ')

    names_2_8 = generate_names(names, 2, 8)
    names_2_9 = generate_names(names, 2, 9)
    names_2_10 = generate_names(names, 2, 10)

    total_2 = names_2_8 | names_2_9 | names_2_10
    generate_name_list(total_2, 2)

    names_3_8 = generate_names(names, 3, 8)
    names_3_9 = generate_names(names, 3, 9)
    names_3_10 = generate_names(names, 3, 10)
    names_3_11 = generate_names(names, 3, 11)
    names_3_12 = generate_names(names, 3, 12)
    names_3_13 = generate_names(names, 3, 13)
    names_3_14 = generate_names(names, 3, 14)

    total_3 = names_3_8 | names_3_9 | names_3_10 | names_3_11 | names_3_12 | names_3_13 | names_3_14
    generate_name_list(total_3, 3)

    names_4_12 = generate_names(names, 4, 12)
    names_4_13 = generate_names(names, 4, 13)
    names_4_14 = generate_names(names, 4, 14)
    names_4_15 = generate_names(names, 4, 15)
    names_4_16 = generate_names(names, 4, 16)

    total_4 = names_4_12 | names_4_13 | names_4_14 | names_4_15 | names_4_16
    generate_name_list(total_4, 4)

    names_5_25 = generate_names(names, 5, 25)

    total_5 = names_5_25
    generate_name_list(total_5, 5)