import os

from pywaclient.api import BoromirApiClient


if __name__ == '__main__':
    client = BoromirApiClient(
        name='stuff',
        url='',
        version='1.0.0',
        application_key=os.getenv('APPLICATION_KEY'),
        authentication_token=os.getenv('AUTHENTICATION_TOKEN')
    )



    for i in client.rpg_system.list():
        print(i)


    for b in client.block_folder.blocks(-1):
        print(b)