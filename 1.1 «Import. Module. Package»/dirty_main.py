from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'{datetime.today():%Y-%B-%d}')
    print(datetime.now().strftime('%Y-%B-%d'))
