# Игрок загадывает число от 1 до 100, а компьютер
# предлагает варианты, пока не угадает
import random

# заводим переменные
max = 100
min = 0
gipoteza = ''
count = 1
otklik = ''

# приветствие
print ('\tЗагадайте число от 1 до 100')
print ('Я буду пытаться его отгадать, а вы говорите мне больше ваше число чем мое предположение или меньше')

input ("\n\nНажмите любую кнопку для продолжения..")

# тело программы

while True:
    gipoteza = random.randint(min, max)
    print (gipoteza)
    print ('Введите 1 если загаданное число БОЛЬШЕ моего')
    print ('Введите 2 если загаданное число МЕНЬШЕ моего')
    print ('Введите 3 если я УГАДАЛ')
    otklik = int(input())
    if otklik == 1:
        min = gipoteza
    elif otklik == 2:
        max = gipoteza
    elif otklik == 3:
        print('Ура я угадал')
        break
    else:
        print('так не честно')

input ("\n\nНажмите Enter, чтобы выйти")
