import requests


if __name__ == '__main__':
    url = 'https://kaikki.org/dictionary/All%20languages%20combined/kaikki.org-dictionary-all.json'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open('kaikki.org-dictionary-all.json', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
