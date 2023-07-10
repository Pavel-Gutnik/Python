# Задача 34: Винни пух.

poetry = input("Введите стих: ").lower().split() 
vowel = [sum(x in "уеыаоэяию" for x in lin) for lin in poetry]
if len(set(vowel)) == 1 :
    print("--- Парам пам-пам ---")
else: print("--- Пам парам ---") 
# ---------- решение 2 ------------------
# alp = "аеёиоуыэюя"
# word_sug = input().split()
# vowel_letters = [sum([True for j in word if j.lower() in alp]) for word in word_sug]

# if all(vowel_letters) and len(set(vowel_letters)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")
# ----------- решение 3 -----------------
# def rhythm(str):
#     str = str.split()
#     list = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list.append(result)
#     return len(list) == list.count(list[0])
# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()
# if rhythm(str):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
#--------------------------------------------