# Задача 24: Черника

n = int(input('Введите кол-во кустов: '))
while n < 3:
    n = int(input('Ошибка! Введите не менее 3-х кустов: '))
berries = list(map(int, input(f'Введите {n} чисел через пробел: ').split()))
n = len(berries)
berries = berries + berries[:2]
m = 0
for i in range(n):
    m = max( m, berries[i] + berries[i+1] + berries[i+2] )
print(f'Максимум ягод  = {m}')

# n = int(input('введи кол-во кустов: '))
# bushes = [int(i) for i in input(f'введи {n} цифр через пробел: ').split()]
# bush_max = 0
# for i in range(n):
#     bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1 if i < n - 1 else 0]
#     if bush_sum > bush_max:
#             bush_max = bush_sum
# print(bush_max)