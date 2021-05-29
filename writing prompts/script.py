import csv
import json
from typing import Any


def write_file(data: Any, filename: str):
    with open(f'{filename}.json', 'w') as fp:
        json.dump(data, fp, ensure_ascii=False, indent='    ')


def create_payload_dict(variable: str):
    router = dict()
    router[variable] = dict()
    return router, router[variable]


if __name__ == '__main__':
    with open('article-template-core.csv', 'r') as fp:
        reader = csv.reader(fp, dialect='unix')
        select_template_generator, select_template = create_payload_dict('values')
        new_article_link_router, new_article_link = create_payload_dict('new-article-link')
        prompt_intro_router, prompt_intro = create_payload_dict('prompt-intro')

        count = 1
        for row in reader:
            if count == 1:
                count += 1
                continue
            select_template[row[0]] = row[1]
            new_article_link[row[0]] = row[2]
            prompt_intro[row[0]] = row[3]

    write_file(select_template_generator, 'select-template-generator')
    write_file(new_article_link_router, 'new-article-link-transformer')
    write_file(prompt_intro_router, 'prompt-intro-transformer')
