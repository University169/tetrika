# a = [12, 3, 51, 2, 17, 49, 80, 1, 4, 37]
def search_pairs(array, k):
    n = len(array)
    b = []
    for i in range(n-1):
        for j in range(i, n-1):
            if (array[i] + array[j]) == k:
                t_direct = tuple((array[i], array[j]))
                t_inverse = tuple((array[i], array[j]))
                if (t_direct not in b) and (t_inverse not in b):
                    b.append(tuple((array[i], array[j])))
    return b


def search_pairs_second(array, k):
    n = len(array)
    b = []
    for i in range(n-1):
        for j in range(i, n-1):
            if (array[i] + array[j]) == k:
                b.append(tuple((array[i], array[j])))
    return list(set(b))


print(search_pairs_second([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

# OUT: >> [(1, 4), (2, 3)]

"""
- Сложность алгоритма O(n**2)
- Можно оптимизировать (см реализацию ex1_optima.py)
"""