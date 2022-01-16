# Анаграммы (word jumble)
#
# Компьютер выбирает какое либо слово и хаотически переставляет его буквы
# Задача игрока - восстановить исходное слово

import random

# создаем последовательность слов
WORDS = ('белый', 'птица', 'мяч', 'земля')
# случайным образом выберем слово из последовательности
word = random.choice(WORDS)
correct = word
# создадим анаграму выбранного слова, в которой буквы будут расставленны хаотично
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

# блок подсказок
podskazka = ''
if correct == 'белый':
    podskazka = 'как черный, только наоборот'
if correct == 'птица':
    podskazka = 'херня с перьями, но не шляпа'
if correct == 'мяч':
    podskazka = 'одна таня его проебала'
if correct == 'земля':
    podskazka = 'все там будем'


# начало игры
print(
'''
        Добро пожаловать в игру "Анаграммы"!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
        (для выхода нажмите Enter не вводя своей версии)
'''
)
print('Вот анаграмма', jumble)
count = 0
points = 0
guess = input('\nПопробуйте отгадать исходное слово: ')
while guess != correct and guess != '':
    print('К сожалению. вы не правы..')
    count += 1
    points -= 1
# ветвление вызова подсказки
    call_help = input('Если нужна подсказка, введите "да", если нет нажмите Enter:')
    if call_help == 'да':
        print('\t\t', podskazka)
        points -= 3
    guess = input('Попробуйте отгадать исходное слово: ')

if guess == correct:
    points += 10
    print('Да именно так, вы отгадали')
    print('Вы заработали', points, 'очков')
print('Спасибо за игру, вы отгадали с', count+1, 'попыток')