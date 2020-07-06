"""
x1y1 - x2y2 один прямоугольник
x3y3 - x4y4 второй прямоугольник
Есть ли у них хотя бы одна общая точка ?
"""

# есть недостаток - я проверяю x3y3 и x4y4, но не учитываю, что в первый прямоугольник может попасть
# какая-либо из двух других вершин второго прямоугольника, а не одна из тех, что даны по условию !

def rectangles(x_coord, y_coord):
    x1 = x_coord[0]
    y1 = y_coord[0]
    x2 = x_coord[1]
    y2 = y_coord[1]
    x3 = x_coord[2]
    y3 = y_coord[2]
    x4 = x_coord[3]
    y4 = y_coord[3]
    result = False
    if x1 == x2 or y1 == y2:
        print('Прямоугольник вырожденный')
    elif x1 > x2:
        # x1 правее x2
        if y1 > y2:
            if (x2 <= x3 <= x1) and (y2 <= y3 <= y1) or (x2 <= x4 <= x1) and (y2 <= y4 <= y1):
                result = True
            # y1 выше y2
        else:
            if (x2 <= x3 <= x1) and (y1 <= y3 <= y2) or (x2 <= x4 <= x1) and (y1 <= y4 <= y2):
                result = True
            # y2 выше y1
    else:
        # x2 правее x1
        if y1 > y2:
            if (x1 <= x3 <= x2) and (y2 <= y3 <= y1) or (x1 <= x4 <= x2) and (y2 <= y4 <= y1):
                result = True
            # y1 выше y2
        else:
            if (x1 <= x3 <= x2) and (y1 <= y3 <= y2) or (x1 <= x4 <= x2) and (y1 <= y4 <= y2):
                result = True
            # y2 выше y1
    if result is False:
        x1 = x_coord[2]
        y1 = y_coord[2]
        x2 = x_coord[3]
        y2 = y_coord[3]
        x3 = x_coord[0]
        y3 = y_coord[0]
        x4 = x_coord[1]
        y4 = y_coord[1]
        if x1 > x2:
            # x1 правее x2
            if y1 > y2:
                if (x2 <= x3 <= x1) and (y2 <= y3 <= y1) or (x2 <= x4 <= x1) and (y2 <= y4 <= y1):
                    result = True
                # y1 выше y2
            else:
                if (x2 <= x3 <= x1) and (y1 <= y3 <= y2) or (x2 <= x4 <= x1) and (y1 <= y4 <= y2):
                    result = True
                # y2 выше y1
        else:
            # x2 правее x1
            if y1 > y2:
                if (x1 <= x3 <= x2) and (y2 <= y3 <= y1) or (x1 <= x4 <= x2) and (y2 <= y4 <= y1):
                    result = True
                # y1 выше y2
            else:
                if (x1 <= x3 <= x2) and (y1 <= y3 <= y2) or (x1 <= x4 <= x2) and (y1 <= y4 <= y2):
                    result = True
                # y2 выше y1
    return result


print(rectangles([2, 1, 3, 2], [5, 6, 0, 2, 0]))

