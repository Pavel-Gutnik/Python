# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[N].
a = int(input("Введите количество элементов: "))
n = list()
for i in range(a):
    n.append(input("Введите элементы: ")) 
print(n)
c = list(map(int, n))
x = int(input("Введите число: "))
count =0
for i in range(a):
    if x == c[i]:
        count +=1
print(f'Колличество встреч числа {x} = {count}' )


# N = abs(int(input('Введите количество элементов списка А: ')))
# A_entered = input("Введите через пробел элементы списка: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, которое необходимо найти в списке: '))
#     count = 0
#     for i in range(N):
#         if A_num[i] == X:
#             count += 1
#     print(f'Число {X} встречается в списке A {count} раз') 