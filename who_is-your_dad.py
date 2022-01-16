# переводчик с гикского на русский
# Демонстрирует использование словарей

geek = {'Пушкин':'Пушкина батя',
        'Сталин':'Сталина батя',
        'Путин':'Путина батя'}

choice = None

while choice != '0':
    print(
    '''
    Кто батя
    0 - Выйти
    1 - найти, что батя чувака
    2 - Добавить чувака
    3 - Изменить батю
    4 - Удалить чувака, вместе с батей
    '''
    )
    choice = input('Ваш выбор: ')
    print()
# выход
    if choice == '0':
        print('До свидания')
    elif choice == '1':
        term = input('Какой чувак вас интересует?')
        if term in geek:
            definition = geek[term]
            print('\n', term, 'означает', definition)
        else:
            print('\nУвы, этот чувак мне не знаком')
    elif choice == '2':
        term = input('Кого вы хотите добавить?')
        if term not in geek:
            definition = input('\nКто его батя: ')
            geek[term] = definition
            print('\nЧувак', term, 'добавлен в словарь.')
        else:
            print('\nТакой Чувак уже есть!.')
    elif choice == '3':
        term = input('Какому чуваку вы хотите сменить батю?')
        if term in geek:
            definition = input('\nВпишите нового батю: ')
            geek[term] = definition
            print('\nБатю', term, 'обновили.')
        else:
            print('\nТакого чувака пока нет, попробуйте добавить его в словарь.')
    elif choice == '4':
        term = input('Какого чувака вы хотите удалить?')
        if term in geek:
            del geek[term]
            print('\nЧувак', term, 'удален.')
        else:
            print('\nНичем не могу помочь. Чувака', term, ' нет в словаре.')
    else:
        print('Извините, в меню нет пункта', choice)

input('\n Нажмите Enter чтобы выйти')
print (geek.keys())
print (geek.values())
print (geek.items())