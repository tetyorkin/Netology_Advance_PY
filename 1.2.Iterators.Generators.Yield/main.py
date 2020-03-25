import json
from urllib.parse import quote


class Country:

    def __init__(self, path):
        self.patch = path
        self.file = open(self.patch)

    def __iter__(self):
        return self

    def __next__(self):
        list_country = []
        file_content = self.file.read()
        try:
            country_str = json.loads(file_content)
            for country in country_str:
                country_name = country['name']['common']
                translations_raw = country['translations']['rus']['common']
                translations = translations_raw.replace(' ', '_')
                url_rus = f"https://ru.wikipedia.org/wiki/{translations}"
                list_country.append(f'{country_name} - {url_rus}')
        except json.decoder.JSONDecodeError:
            raise StopIteration
        return list_country


# Функция записи полученных данных в файл
def write_file(data_in):
    with open('countries_url.txt', 'w', encoding='utf-8') as file:
        data_raw = ',  '.join(data_in)
        data = data_raw.replace(',  ', '\n')
        file.write(str(data))


if __name__ == '__main__':
    url_country = Country('countries.json')
    write_file(url_country.__next__())
