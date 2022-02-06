"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.

"""

import chardet
import subprocess
import platform


def penguin_show(site_name):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '1', site_name]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


penguin_show('yandex.ru')
print('****************')
penguin_show('youtube.com')
