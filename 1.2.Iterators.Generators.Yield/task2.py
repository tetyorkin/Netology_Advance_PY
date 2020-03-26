import hashlib


# Пишем генератор, который будет возвращать md5 хеш строки из файла со списком стран и ссылок на их странице в Википедии
# Проверку проводил на ресурсе https://www.md5hashgenerator.com/
def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        for file_content in f.readlines():
            string = file_content
            to_obj_md5 = hashlib.md5(string.strip().encode())
            hash_md5 = to_obj_md5.hexdigest()
            yield hash_md5


if __name__ == '__main__':
    for md5_hash in read_file('countries_url.txt'):
        print(md5_hash)
