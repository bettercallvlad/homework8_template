import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    2 - Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    1 - Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    3- Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def copy_data(source: str, dest: str, num_row: int):
    """
    4 - Функция для копирования указанной строки из одного файла в другой
    source: str     - имя исходного файла
    dest: str       - имя файла куда переносим
    num_row: int    - номер копируемой строки
    """
    with open(source, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    if num_row > len(list_1):
        print (f'В фале нет строки {num_row}')
    else:
        with open(dest, "a", encoding="utf-8") as file:
            transfer_line = list_1[num_row]
            file.write(f"{transfer_line}")
            print ('Строка скопирована в новый файл')

def transfer_data(source: str, dest: str, num_row: int):
    """
    5 - Функция для переноса указанной строки из одного файла в другой
    source: str     - имя исходного файла
    dest: str       - имя файла куда переносим
    num_row: int    - номер переносимой строки
    """
    with open(source, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    print(list_1)
    if num_row > len(list_1):
        print (f'В фале нет строки {num_row}')
    else:
        with open(dest, "a", encoding="utf-8") as file:
            transfer_line = list_1[num_row]
            file.write(f"{transfer_line}")
            print ('Строка скопирована в новый файл')

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - Копирование записи в другой файл
5 - Перенос записи в другой файл
"""

file = "Text.txt"
file_dest = "Text_dest.txt"

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        row_num = int(input("Какую строку нужно скопировать: "))
        copy_data(file, file_dest, row_num)
    elif mode == 5:
        row_num = int(input("Какую строку нужно перенести: "))
        transfer_data(file, file_dest, row_num)
