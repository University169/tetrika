"""
В этой задаче, помимо алгоритма, нужно указать ответ числом.

Есть файл с именами. Нужно выполнить следующие действия и посчитать результат:

1) Отсортировать все имена в лексикографическом порядке
2) Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке
(индексация начинается с 1).
Например, если MAY находится на 63 месте в списке, то результат для него будет 63 * 39 = 2457.
4) Просуммировать произведения из третьего пункта по всем именам из файла.

В качестве ответа надо прислать код и число из пункта 4.
"""


def word_sum(word, letter_dictionary):
    word_letter = list(word)
    s = 0
    for letter in word_letter:
        s += letter_dictionary[letter]
    return s


names_original_data = open('names.txt', 'r')
names_list_original = names_original_data.read().strip().replace('"', "").split(',')
names_list_sorted = sorted(names_list_original)
# print(names_list_sorted)
n = len(names_list_sorted)  # количество имен всего изначально

dictionary_capital = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                      'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                      'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

result = 0
for i in range(n):
    functional = word_sum(names_list_sorted[i], dictionary_capital)
    result += (i + 1) * functional
    # print(f'{i + 1} {names_list_sorted[i]} = {functional} => result = {result}')
print(result)

# Ответ: 871853874
