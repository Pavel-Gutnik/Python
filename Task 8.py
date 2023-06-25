# Задача 8: Шоколадка.
n = int(input("Введите размер N: "))
m = int(input("Введите размер M: "))
k = int(input("Введите количество K: "))
if k < m * n and (k % m == 0 or k % n == 0):
    print(" Да :)")
else:
    print(" Нет :(")
