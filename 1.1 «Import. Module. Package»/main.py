from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt

if __name__ == '__main__':
    # Задание 1 и 2
    calculate_salary()
    get_employees()
    # Задание 3
    print(f'{dt.datetime.today():%Y-%B-%d}')
    print(dt.datetime.now().strftime('%Y-%B-%d'))

