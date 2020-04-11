import hashlib
import datetime as dt


def logger(func):
    def foo(*args, **kwargs):
        date_time = dt.datetime.now()
        name = func.__name__
        result = func(*args, **kwargs)
        with open('decorator.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата и время: {date_time:%b.%d %H:%M}\n'
                       f'Имя функции: {name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Возвращаемое значение: {result}')
        return foo

    return foo


# Функция из задания возвращения хеша md5 из строки файла
@logger
def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        for file_content in f.readlines():
            string = file_content
            to_obj_md5 = hashlib.md5(string.strip().encode())
            hash_md5 = to_obj_md5.hexdigest()
            return hash_md5


if __name__ == '__main__':
    read_file('countries_url.txt')
