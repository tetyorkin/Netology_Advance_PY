import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'


def translate(first_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': first_lang,
        'lang': '{}'.format(to_lang.lower())
    }

    response = requests.get(URL, params=params)
    text = response.json()
    return text


if __name__ == '__main__':
    print(translate('hi')['text'][0])
