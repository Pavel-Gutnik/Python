# Задача 2: Сумма цифр числа.
# n = int(input("Введите число: "))
# sum = 0
# while n > 0:
#     x = n % 10
#     sum = sum + x
#     n = n // 10
# print(sum)
# ---------------------------------------------
# Задача 2. решение через функцию.
# n = int(input("Введите трёхзначное число: "))
# def getSum(n):
#   sum = 0
#   while n != 0:
#       sum = sum + (n % 10)
#       n = n // 10
#   return sum
# print(getSum(n))
# ---------------------------------------------
# Задача 2. решение с условием трёхзначности числа.
n = int(input("Введите трёхзначное число: "))
sum = 0
while n < 100 or n > 999:
    n = int(input("Ошибка! Введите трёхзначное число: "))
while n > 0:
    sum = sum + (n % 10)
    n = n // 10
print(sum)
# ---------------------------------------------
