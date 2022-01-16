# Данный файл включает в себя мелкие программки для проработки
# тем списков и словарей из главы 5 книги по python.
# Все программы разделены абзацем
# не нужные к исполнению в моменте закомментированы

# Арсенал героя 3.0
# # демонстрирует работу со списками
# # создадим список с несколькими элементами и выведем его с помощью цикла for
# inventory = ['меч',
#              'кольчуга',
#              'щит',
#              'целебное снадобье']
# print('\nИтак в вашем арсенале: ')
# for item in inventory:
#     print(item)
# input('\n Нажмите Enter чтобы продолжить')
#
# # найдем длину списка
# print('Сейчас в вашем распоряжении', len(inventory), 'предмета/ов')
# input('\n Нажмите Enter чтобы выйти')
#
# # проверка принодлежности к списку с помощью in
# if 'целебное снадобье' in inventory:
#     print('Вы еще поживете и повоюете')
#
# # вывод одного из элементов списка с определенным индексом
# index = int(input('\nВведите индекс одного из предметов арсенала: '))
# print('Под индексом', index, 'в арсенале находится', inventory[index])
#
# # отобразим срез
# start = int(input('\nВведите начальный индекс среза: '))
# finish = int(input('\nВведите конечный индекс среза: '))
# print('Срез inventory[', start, ':', finish, '] - это', end=' ')
# print(inventory[start:finish])
#
# # соединим два списка
# chest = ['золото', 'драгоценные камни']
# print('Вы нашли ларец, вот что в нем есть:')
# print(chest)
# print('Все что нашли, вы положили в рюкзак')
# inventory += chest
# print('Теперь  в вашем распоряжении:')
# print(inventory)
#
# # присваеваем значение элементу по индексу
# print('Вы обменяли меч на арбалет')
# inventory[0] = 'Арбалет'
# print('Теперь ваш арсенал содержит следующие предметы:')
# print(inventory)
#
# # припсываем значение элементам по срезу индексов
# print('За золото и драгоценные камни вы купили магический кристалл, способный предсказывать будущее.')
# inventory[4:6] = ['магический кристалл']
# print('Теперь ваш арсенал содержит следующие предметы:')
# print(inventory)
#
# # удаляем элемент
# print('В тяжком бою, вы раздробили щит.')
# del inventory[2]
# print('Вот, что осталось в арсенале:')
# print(inventory)
#
# # удаляем срез
# print('Воры лишили вас арбалета и кольчуги')
# del inventory[:2]
# print('В арсенале теперь только:')
# print(inventory)

# Рекорды
# Демонстрирует списочные методы
# scores = []
# choice = None
#
# while choice != '0':
#     print(
#     '''
#     Рекорды
#     0 - Выйти
#     1 - Показать рекорды
#     2 - Добавить рекорд
#     3 - Удалить рекорд
#     4 - Сортировать список
#     '''
#     )
#     choice = input('Ваш выбор: ')
#     print()
# # выход
#     if choice == '0':
#         print('До свидания')
# # вывод лучших результатов на экран
#     elif choice == '1':
#         print('Рекорды')
#         for score in scores:
#             print(score)
# # добавление рекорда
#     elif choice == '2':
#         score = int(input('Введите свой рекорд:'))
#         scores.append(score)
# # удаление рекорда
#     elif choice == '3':
#         score = int(input('Какой из рекордов удалить?:'))
#         if score in scores:
#             scores.remove(score)
#         else:
#             print('Результат', score, 'не содержится в списке рекордов.')
# # сортировка рекордов
#     elif choice == '4':        scores.sort(reverse=True)
# # непонятный пользовательский ввод
#     else:
#         print('Извините, в меню нет пункта', choice)
#
# input('\n Нажмите Enter чтобы выйти')

# список слов в случайном порядке
# import random
# spisok = ['мир', 'труд', 'май', 'жопа']
# copy = spisok[:]
# for i in range(len(spisok)):
#     used = random.choice(copy)
#     print(used)
#     copy.remove(used)
# print(spisok)
# print(copy)

# генератор персонажей
skill_point = 30
sila = 0
lovkost = 0
zdorovie = 0
mudrost = 0
choice = ''
subchoice = ''

while choice != '0':
    print('Сейчас ваши параметры выглядят так:')
    print('Сила:', sila, '\t\t(нажмите 1, чтобы настроить)')
    print('Ловкость:', lovkost, '\t\t(нажмите 2, чтобы настроить)')
    print('Здоровье:', zdorovie, '\t\t(нажмите 3, чтобы настроить)')
    print('Мудрость:', mudrost, '\t\t(нажмите 4, чтобы настроить)')
    print('Нераспределенных очков:', skill_point)
    choice = input('Укажите какой параметр будем качать("0" для выхода):')
    print()
    if choice == '0':
        print('До свидания')
#сила
    elif choice == '1':
        print('Разбираемся с силой. Выберите 0 для выхода в меню')
        subchoice = input('Введите "1", чтобы прибавить очков к силе или "2" чтобы убрать очки силы')
        if subchoice == '0':
            input('\n Нажмите Enter чтобы продолжить')
        elif subchoice == '1':
            number_skill_points = int(input('Сколько очков вы хотите прибавить к силе'))
            if skill_point - number_skill_points < 0:
                print('Свободных очков не хватает')
            else:
                sila += number_skill_points
                skill_point -= number_skill_points
        elif subchoice == '2':
            number_skill_points = int(input('Сколько очков вы хотите убрать'))
            if sila - number_skill_points < 0:
                print('Сила не можт быть меньше нуля')
            else:
                sila -= number_skill_points
                skill_point += number_skill_points
        else:
            print('Команда непонятна')
# ловкость
    elif choice == '2':
        print('Разбираемся с ловкостью. Выберите 0 для выхода в меню')
        subchoice = input('Введите "1", чтобы прибавить очков к ловкости или "2" чтобы убрать очки ловкости')
        if subchoice == '0':
            input('\n Нажмите Enter чтобы продолжить')
        elif subchoice == '1':
            number_skill_points = int(input('Сколько очков вы хотите прибавить к ловкости'))
            if skill_point - number_skill_points < 0:
                print('Свободных очков не хватает')
            else:
                lovkost += number_skill_points
                skill_point -= number_skill_points
        elif subchoice == '2':
            number_skill_points = int(input('Сколько очков вы хотите убрать'))
            if lovkost - number_skill_points < 0:
                print('Ловкость не можт быть меньше нуля')
            else:
                lovkost -= number_skill_points
                skill_point += number_skill_points
        else:
            print('Команда непонятна')
# здоровье
    elif choice == '3':
        print('Разбираемся со здоровьем. Выберите 0 для выхода в меню')
        subchoice = input('Введите "1", чтобы прибавить очков к здоровью или "2" чтобы убрать очки здоровья')
        if subchoice == '0':
            input('\n Нажмите Enter чтобы продолжить')
        elif subchoice == '1':
            number_skill_points = int(input('Сколько очков вы хотите прибавить к здоровью'))
            if skill_point - number_skill_points < 0:
                print('Свободных очков не хватает')
            else:
                zdorovie += number_skill_points
                skill_point -= number_skill_points
        elif subchoice == '2':
            number_skill_points = int(input('Сколько очков вы хотите убрать'))
            if zdorovie - number_skill_points < 0:
                print('Здоровье не можт быть меньше нуля')
            else:
                zdorovie -= number_skill_points
                skill_point += number_skill_points
        else:
            print('Команда непонятна')
# мудрость
    elif choice == '4':
        print('Разбираемся со мудростью. Выберите 0 для выхода в меню')
        subchoice = input('Введите "1", чтобы прибавить очков к мудрости или "2" чтобы убрать очки мудрости')
        if subchoice == '0':
            input('\n Нажмите Enter чтобы продолжить')
        elif subchoice == '1':
            number_skill_points = int(input('Сколько очков вы хотите прибавить к мудрости'))
            if skill_point - number_skill_points < 0:
                print('Свободных очков не хватает')
            else:
                mudrost += number_skill_points
                skill_point -= number_skill_points
        elif subchoice == '2':
            number_skill_points = int(input('Сколько очков вы хотите убрать'))
            if mudrost - number_skill_points < 0:
                print('Мудрость не можт быть меньше нуля')
            else:
                mudrost -= number_skill_points
                skill_point += number_skill_points
        else:
            print('Команда непонятна')

