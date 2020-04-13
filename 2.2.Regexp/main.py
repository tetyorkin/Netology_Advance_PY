# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
def phone(contact_list):
    last_name = re.compile(r"\['(?P<last_name>\w+)(',\n\s+'|\s|'.\s')(?P<fist_name>firs\w+|[А-я]+)(',\n\s+'|\s|'.\s')"
                           r"(?P<surname>sur\w+|[А-я]+|)(',\n\s+'',\n\s+'',\n\s+'|',\s'', '', '|', '', '|',\n\s+')"
                           r"(?P<organization>\w+|)(',\n\s+'|)(?P<position>pos\w+|\w+.+\n\s+.+)", re.M)
    list_last_name = []
    for match in last_name.finditer(str(contact_list)):
        list_last_name += [match.group('last_name'), match.group('fist_name'), match.group('surname'),
                           match.group('organization'), match.group('position')]
    print(list_last_name)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)

if __name__ == '__main__':
    phone(contacts_list)
