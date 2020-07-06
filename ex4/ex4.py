"""
Поиск индекса последней единицы в списке, где сперва идут единицы, а затем нули.
"""


def search(input_list):
    a = 0
    b = len(input_list) - 1
    if input_list[0] == 0:
        return -1
    elif input_list[-1] == 1:
        return b

    logic = True
    c = len(input_list)
    while logic:
        d = a + (c // 2)
        if input_list[d] == 1:
            a = a + (c // 2) + 1
        else:
            b = a + (c // 2) - 1
        c = b - a + 1
        if a == b:
            if input_list[a] == 1:
                return a
            else:
                return a - 1
        elif c == 2:
            if input_list[b] == 1:
                return b
            elif input_list[a] == 1:
                return a
            else:
                return a - 1


print(search([1, 1, 1, 1, 0, 0, 0, 0, 0]))
# >> OUT: 3
