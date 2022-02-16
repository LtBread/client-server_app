""" 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:

    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
    считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
    значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
    os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для
    хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:

        «Изготовитель системы»,
        «Название ОС»,
        «Код продукта»,
        «Тип системы».

    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
    (также для каждого файла);

    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
    получение данных через вызов функции get_data(), а также сохранение подготовленных данных в
    соответствующий CSV-файл;

    Проверить работу программы через вызов функции write_to_csv().

"""

import re
import csv
from chardet import detect


def get_data(files):

    header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    raw_strings_for_search = [
        r'(?<=Изготовитель системы:)\s*.*',
        r'(?<=Название ОС:)\s*.*',
        r'(?<=Код продукта:)\s*.*',
        r'(?<=Тип системы:)\s*.*',
    ]

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for file in files:
        # detect encoding
        researched = b''
        with open(file, 'rb') as f:
            chunk = 900
            while True:
                part = f.read(chunk)
                if not part:
                    break
                researched += part
        encoding = detect(researched)['encoding']

        # read the entire file
        with open(file, encoding=encoding) as f:
            data = f.read()

        # parse
        def aggregate(row_string, empty_list):
            pattern = re.compile(row_string)
            result = re.search(pattern, data)
            if result:
                empty_list.append(result.group().strip())
            else:
                empty_list.append('None')

        list_of_lists = [os_prod_list, os_name_list, os_code_list, os_type_list]
        for raw, li in zip(raw_strings_for_search, list_of_lists):
            aggregate(raw, li)

    # transposition
    headless_list = [os_prod_list, os_name_list, os_code_list, os_type_list]
    main_data = [[headless_list[j][i] for j in range(len(headless_list))] for i in range(len(headless_list[0]))]
    main_data.insert(0, header)
    return main_data


def write_to_csv(files_in, file_out):
    with open(file_out, 'w', encoding='utf-8', newline='') as f_out:
        f_writer = csv.writer(f_out)
        f_writer.writerows(get_data(files_in))


if __name__ == '__main__':
    source_files = 'info_1.txt', 'info_2.txt', 'info_3.txt',
    destination_file = 'data_report.csv'
    write_to_csv(source_files, destination_file)

