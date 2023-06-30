# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[N].
# a = int(input("Введите количество элементов: "))
# n = list()
# for i in range(a):
#     n.append(input("Введите элементы: ")) 
# print(n)
# c = list(map(int, n))
# x = int(input("Введите число: "))
# count =0
# for i in range(a):
#     if x == c[i]:
#         count +=1
# print(f'Количество встреч числа {x} = {count}' )

# Задача 16: второй вариант.
N = abs(int(input('Введите количество элементов списка: ')))
ent = input("Введите через пробел элементы списка: ").split()
num = list(map(int, ent))
if len(num) != N:
    print('Элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число которое необходимо найти: '))
    count = 0
    for i in range(N):
        if num[i] == x:
            count += 1
    print(f'Количество встреч числа {x} = {count}') 