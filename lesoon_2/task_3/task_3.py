""" 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в
файле YAML-формата. Для этого:

    Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
    третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
    кодировке ASCII (например, €);

    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
    с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;

    Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

"""

import yaml
from yaml.loader import UnsafeLoader

data = {

    'first': [1, 2, 3],
    'second': 4,
    'third': {
        'evro': '\u20ac',
        'dollar': '\u0024',
        'ruble': '\u20bd',
    }
}
print(data['third'])

with open('file.yaml', 'w', encoding='utf-16') as f_out:
    yaml.dump(data, f_out, default_flow_style=False, allow_unicode=True)

with open('file.yaml', encoding='utf-16') as f_in:
    retrieved_data = yaml.load(f_in, Loader=UnsafeLoader)

print(retrieved_data)
print(data == retrieved_data)
