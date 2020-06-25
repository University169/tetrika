Задания
========================================================
Задание 1

Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел из массива, сумма которых равна k.

Примечание: под уникальностью понимается следующее: если ответу удовлетворяет несколько пар вида (a, b) и (b, a), то достаточно вывести только одну пару (a, b).


def search_pairs(array, k):
....


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

OUT: >> [(1, 4), (2, 3)]


Вопросы:
- Какая сложность у вашего алгоритма?
- Можно ли его оптимизировать?

-------------------------------------------------------------------

Задание 2

В этой задаче, помимо алгоритма, нужно указать ответ числом.

Есть файл с именами (https://yadi.sk/i/97rbNP2ucGoAKw). Нужно выполнить следующие действия и посчитать результат:

1) Отсортировать все имена в лексикографическом порядке
2) Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке (индексация начинается с 1). Например, если MAY находится на 63 месте в списке, то результат для него будет 63 * 39 = 2457.
4) Просуммировать произведения из третьего пункта по всем именам из файла.

В качестве ответа надо прислать код и число из пункта 4.

-------------------------------------------------------------------

Задание 3

Факториал числа n равен произведению всех чисел от 1 до n, то есть:
n! = 1 * 2 * 3 * ... * n

Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.

def get_zeros(n):
....

print(get_zeros(5))
OUT: >> 1

print(get_zeros(12))
OUT: >> 2


Вопросы:
- Какая сложность у вашего алгоритма?