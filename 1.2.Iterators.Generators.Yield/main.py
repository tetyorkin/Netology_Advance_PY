import json
from urllib.parse import quote



def read_file(file_name):
    with open(file_name) as f:
        file_content = f.read()
        templates = json.loads(file_content)
        return templates


def find_country(file_name):
    contry
    list_country = []
    for country in read_file(file_name):
        country_name = country['name']['common']
        translations = country['translations']['rus']['common']
        url_rus = f"https://ru.wikipedia.org/wiki/{quote(translations)}"
        list_country.append(f'{country_name:<20} - {url_rus}')
    return list_country


def write_file(file_name):
    with open('countries_url.txt', 'w', encoding='utf-8') as file:
        data_raw = ',  '.join(find_country(file_name))
        data = data_raw.replace(',  ', '\n')
        file.write(str(data))


if __name__ == '__main__':
    write_file('countries.json')
