"""4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить обратное
преобразование (используя методы encode и decode).

"""


def encoder(words):
    return [word.encode('utf-8') for word in words]


def decoder(words):
    return [word.decode('utf-8') for word in words]


words_4 = 'разработка', 'администрирование', 'protocol', 'standard'

bytes_words = encoder(words_4)
for word in bytes_words:
    print(word, type(word))

print('*************************')

rebytes_words = decoder(bytes_words)
for word in rebytes_words:
    print(word, type(word))

