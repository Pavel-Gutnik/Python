# Задача 12: Отгадай числа.
s = int(input("Сумма = "))
p = int(input("Произведение = "))
c = 0
for i in range(s + p):
    if c:
        break
    for j in range(s + p):
        if i + j == s and i * j == p:
            c = 1
            print(("Загаданы числа ->"),i,("и"), j)
                