import math as m

p = (x, y)


def cal(x1, y1, x2, y2):
    return m.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)


print(cal(2, 3, 5, 7))
