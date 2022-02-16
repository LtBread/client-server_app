""" 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
    Создать функцию write_order_to_json(), в которую передается 5 параметров —

        товар (item),
        количество (quantity),
        цена (price),
        покупатель (buyer),
        дата (date).

    Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать
    величину отступа в 4 пробельных символа;

    Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

"""

import json


def write_order_to_json(item, quantity, price, buyer, date):

    new_data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json', encoding='utf-8') as json_statham:
        data = json.load(json_statham)

    data['orders'].append(new_data)

    with open('orders.json', 'w', encoding='utf-8') as json_statham:
        json.dump(data, json_statham, indent=4)


if __name__ == '__main__':
    order = {
        'item': 'watermelon',
        'quantity': 150,
        'price': 300.0,
        'buyer': 'Tomas Anderson',
        'date': '12-12-2012',
    }
    write_order_to_json(**order)
