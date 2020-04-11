import datetime as dt
import requests


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
        return

    return foo


@logger
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://mail.ru/')
