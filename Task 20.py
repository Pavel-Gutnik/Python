
# Задача 20. Scrabble. Не совсем правильное решение,
# не определяется язык без выбора...

# eng = {1:'AEIOULNSTR',2:'DG',3:'BCMP',
#       	4:'FHVWY',5:'K',8:'JZ',10:'QZ'}
# rus = {1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',
#       	4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
# N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
# word = input('Введите слово: ').upper()
# if N == 1:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
# elif N == 0:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
# else:
#     print('Вы мухлюете и играете не по правилам!')

# -------------------------------------------------------
# Задача 20. Scrabble. Решение с функцией.

# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# en = {1:'AEIOULNSTR',2:'DG',3:'BCMP',
#       	    4:'FHVWY',5:'K',8:'JZ',10:'QZ'}
# ru = {1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',
#       	    4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
# text = input("Введите слово: ").upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in en.items() if i in v]))
# -------------------------------------------------------

# Задача 20: Scrabble.

en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
Eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
      4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
Rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
      4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
word = input('Введите слово: ')
if word[0].lower() in en:
    sum = 0
    for letter in word:
        for key, value in Eng.items():
            if letter.upper() in value:
                sum += key
    print(("Стоимость слова"), "=", (sum))
else:
    if word[0].lower() in ru:
        sum = 0
        for letter in word:
            for key, value in Rus.items():
                if letter.upper() in value:
                    sum += key
    print(("Стоимость слова"), "=", (sum))