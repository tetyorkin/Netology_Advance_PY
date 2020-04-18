import csv
import datetime as dt
import re

from pymongo import MongoClient

FILE = 'artists.csv'


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла    """
    with open(csv_file, encoding='utf-8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        list_artist = list(reader)
        new_artist_list = []
        id_artist = 0
        for line in list_artist:
            id_artist += 1
            artist_list = {'_id': id_artist,
                           'Исполнитель': line['Исполнитель'],
                           'Цена': float(line['Цена']),
                           'Место': line['Место'],
                           'Дата': dt.datetime.strptime('2020 ' + line['Дата'], '%Y %d.%m')}
            new_artist_list.append(artist_list)

        db.insert_many(new_artist_list)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    """
    result = list(db.find().sort('Цена', 1))
    for line in result:
        print(line)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    regex = re.compile(name, re.IGNORECASE)
    result = list(db.find({'Исполнитель': regex}).sort('Цена', 1))
    for line in result:
        print(line)


def find_by_date(db):
    """
    Реализовать сортировку по дате мероприятия. Для этого вам потребуется строку с датой в csv-файле приводить
    к объекту datetime (можете считать, что все они текущего года) и сохранять его.
    Найти билеты по дате (Всё мероприятия с 1 по 30 июля.  $gte >=, $lte <=). Также отсортировал по дате
    """
    day_start = dt.datetime(2020, 7, 1)
    day_end = dt.datetime(2020, 7, 30)
    result = list(db.find({'Дата': {'$gte': day_start, '$lte': day_end}}).sort('Дата', 1))
    for line in result:
        print(line)


if __name__ == '__main__':
    client = MongoClient()
    netology_db = client['netology_db']
    artist = netology_db['artists']
    read_data(FILE, artist)
    find_cheapest(artist)
    find_by_name('Вася', artist)
    find_by_date(artist)
