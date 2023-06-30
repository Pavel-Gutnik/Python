# Задача 18: Hайти в массиве A[N] самый близкий по величине элемент к заданному числу X.

# Задача 18: не совсем правильно находит ближайший меньший элемент.
# к примеру: [1 2 3 4 5 7 9 12] X = 11 выдаст 9
# a=[int(i) for i in input("Введите через пробел элементы списка: ").split()]
# b=int(input("Введите число: "))
# number = 0
# for i in range(len(a)):
#     if (b - a[i]) < b - number and b - a[i] > 0:
#         number = i
# print(a[number])


# Задача 18: Работает вроде но не пойму как вставить ограничение по вводу...
n = abs(int(input('Введите количество элементов: ')))
a = input("Введите элементы списка: ").split()
c = list(map(int, a))
x = int(input('Введите число x: '))
min = abs(x - c[0])
index = 0
for i in range(1, n):
    count = abs(x - c[i])
    if count < min:
        min = count
        index = i
print(f'Число {c[index]} наиболее близко по величине к числу {x}')            