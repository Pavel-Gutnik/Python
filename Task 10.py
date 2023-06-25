# Задача 10: Переворот монеток решение 1.
# n = int(input("Введите количество монет: "))
# x = 0
# for i in range(n):
#     y = int(input())
#     if y == 1:
#         x += 1
# print(x if x < n / 2 else n - x)
# ---------------------------------------------
# Задача 10: Переворот монеток решение 1.
n = int(input("Введите количество монет: "))
orel = 0
reshka = 0
for i in range(n):
  x = int(input("Введите 0 или 1 -> "))
  if x == 0:
    orel += 1
  else:
    reshka += 1
print(orel if reshka > orel else reshka)