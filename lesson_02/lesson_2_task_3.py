import math


def square(item):
    return item * item


items = math.ceil(float(input("Введите сторону квадрата: ")))
print(f"Площадь квадрата = {square(items)}")
