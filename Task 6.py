# Задача 6: Счастливый билет.
# n = input("Введите номер билета: ")
# s1 = int(n[0]) + int(n[1]) + int(n[2])
# s2 = int(n[3]) + int(n[4]) + int(n[5])
# if s1 == s2:
#     print("Счастливый")
# else:
#     print("Обычный")
# ----------------------------------------------
# Задача 6: Счастливый билет. С использованием ф-ций List и map  
n = int(input("Введите номер билета: "))
d = list(map(int, list(f'{n:06}')))
print(('NO', 'YES')[sum(d[:3])==sum(d[3:])])
