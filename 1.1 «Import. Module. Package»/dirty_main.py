from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    # Задание 1 и 2
    calculate_salary()
    get_employees()
    # Задание 3
    print(f'{datetime.today():%Y-%B-%d}')
    print(datetime.now().strftime('%Y-%B-%d'))
