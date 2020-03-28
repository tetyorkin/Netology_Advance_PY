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


def main():
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)


if __name__ == '__main__':
    main()
