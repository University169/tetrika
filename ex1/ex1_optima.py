"""
Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел из массива,
сумма которых равна k.

Примечание: под уникальностью понимается следующее:
если ответу удовлетворяет несколько пар вида (a, b) и (b, a),
то достаточно вывести только одну пару (a, b).

Вопросы:
- Какая сложность у вашего алгоритма?
- Можно ли его оптимизировать?
"""


def search_pairs(array, k):
    n = len(array)
    A = set()
    B = set()
    M = []
    for i in range(n):
        if array[i] in A:
            if k % 2 == 0 and array[i] == (k // 2):
                M.append(tuple((array[i], array[i])))
                A.remove(array[i])
                B.add(array[i])
        elif array[i] in B:
            pass
        elif (k - array[i]) in A:
            M.append(tuple((k - array[i], array[i])))
            A.remove(k - array[i])
            B.add(k - array[i])
            B.add(array[i])
        else:
            A.add(array[i])
    return M


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

# OUT: >> [(1, 4), (2, 3)]

"""
- Сложность алгоритма O(n)
- Невозможно оптимизировать
"""