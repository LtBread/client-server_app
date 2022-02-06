""" 2. Каждое из слов «class», «function», «method» записать в байтовом
типе без преобразования в последовательность кодов (не используя методы
encode и decode) и определить тип, содержимое и длину соответствующих переменных.

 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно
записать в байтовом типе. Важно: решение должно быть универсальным, т.е. не зависеть 
от того, какие конкретно слова мы исследуем.

"""


def bytes_converter(words):
    return [eval("b" + f"'{word}'") for word in words]


words2 = 'class', 'function', 'method'
words3 = 'attribute', 'класс', 'функция', 'type'

try:
    bytes_words = bytes_converter(words2 + words3)
    for word in bytes_words:
        print(word, type(word), len(word))

except SyntaxError as e:
    print(f'Conversion error: {e.msg} ({e.text})')
