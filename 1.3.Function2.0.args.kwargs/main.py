class Contact:

    def __init__(self, name, last_name, phone, favorite=False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.favorite = favorite
        self.kwargs = kwargs

    def __str__(self):
        user = {'Имя': self.name, 'Фамилия': self.last_name, 'Телефон': self.phone, 'В избранных': self.favorite,
                'Дополнительная информация': self.kwargs}
        string1 = ''
        string2 = ''
        for key, value in user.items():
            # string1 += f'{key}: {value}\n'
            if key == 'Имя':
                string1 += f'{key}: {value}\n'
            elif key == 'Фамилия':
                string1 += f'{key}: {value}\n'
            elif key == 'Телефон':
                string1 += f'{key}: {value}\n'
            elif key == 'Дополнительная информация':
                string1 += f'{key}:\n'
                for key1, value1 in value.items():
                    string2 += f'\t\t{key1}: {value1}\n'
            elif self.favorite:
                string1 += f'{key}: да\n'
            elif not self.favorite:
                string1 += f'{key}: нет\n'
        return string1 + string2


# Задание №2
class PhoneBook:

    def __init__(self, name_book):
        self.name_book = name_book
        self.contact_list = []

    def get_contact(self):
        for contact in self.contact_list:
            print(contact)

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def del_contact(self, phone):
        for contact in self.contact_list:
            if contact.phone == phone:
                self.contact_list.remove(contact)

    def find_favorite(self):
        for contact in self.contact_list:
            if contact.favorite:
                print(contact)

    def find_by_name(self, name, last_name):
        for contact in self.contact_list:
            if contact.name == name and contact.last_name == last_name:
                print(contact)


def main():
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    katy = Contact('Katy', 'Afere', '+71254564564', True, telegram='@katy', email='katy@afere.com')
    print(jhon)
    print(katy)
    # Вывод на экран задания 2 с проверкой всех методов
    print('\nЗадание № 2\n')
    book = PhoneBook('My phone book')
    book.add_contact(jhon)
    book.add_contact(katy)
    book.get_contact()
    book.find_favorite()
    book.find_by_name('Jhon', 'Smith')
    book.del_contact('+71234567809')
    book.get_contact()


if __name__ == '__main__':
    main()
