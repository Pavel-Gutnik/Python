# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# - Вариант 1 - авто рандомный список в диапазоне от -5 до 20, с кол-вом эл-тов 10 ---
import random
list_1 = [random.randint(-5,20) for i in range(10)]
print(list_1)
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
for i in range(len(list_1)):
    if min_value <= list_1[i] <= max_value:
        print(i, end = " ")
    

# - Вариант 2 - список в ручную и вывод в одну строку. ---
# array = list(map(int, input('Введите элементы: ').split()))
# min_value = int(input("Введите минимальное значение: "))
# max_value = int(input("Введите максимальное значение: "))
# print([i for i in range(len(array)) if min_value <= array[i] <= max_value])       