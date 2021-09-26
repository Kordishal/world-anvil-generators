import json
import os

from pywaclient.api import AragornApiClient
from pywaclient.models.world import World

if __name__ == '__main__':
    client = AragornApiClient(
        'SoulLinks Utility',
        'https://www.worldanvil.com/author/SoulLink', 'v1', os.environ['WA_APPLICATION_KEY'], os.environ['WA_AUTH_TOKEN']
    )

    wbtv = World(client, client.world.get('a86b6da9-6ba2-413a-87d9-ee98cbc6d9b9'))

    container = dict()
    randomized_articles = dict()
    container['values'] = randomized_articles

    container_randomized_blocks = dict()
    randomized_article_blocks = dict()
    container_randomized_blocks['values'] = randomized_article_blocks

    count = 0
    for article in wbtv.articles():
        if '#random' in article.tags:
            randomized_articles[f'article-{count}'] = f'@[{article.title}]({article.template}:{article.id})'
            randomized_article_blocks[f'article-{count}'] = f'[articleblock:{article.id}]'
            count += 1

    with open('random-article-link.json', 'w') as fp:
        json.dump(container, fp, ensure_ascii=False, indent='    ')

    with open('random-article-block.json', 'w') as fp:
        json.dump(container_randomized_blocks, fp, ensure_ascii=False, indent='    ')
