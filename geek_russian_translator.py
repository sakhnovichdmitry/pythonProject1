# переводчик с гикского на русский
# Демонстрирует использование словарей

geek = {'404':'Не знать, не владеть информацией',
        'googling':'Гугление, поиск информации в сети',
        'keyboard plague':'Мусор в клавиатуре'}

choice = None

while choice != '0':
    print(
    '''
    Переводчик с гикского на русский
    0 - Выйти
    1 - найти толкование термина
    2 - Добавить термин
    3 - Изменить толкование
    4 - Удалить термин
    '''
    )
    choice = input('Ваш выбор: ')
    print()
# выход
    if choice == '0':
        print('До свидания')
    elif choice == '1':
        term = input('Какой термин вас интересует?')
        if term in geek:
            definition = geek[term]
            print('\n', term, 'означает', definition)
        else:
            print('\nУвы, этот термин мне не знаком')
    elif choice == '2':
        term = input('Какой термин вы хотите добавить?')
        if term not in geek:
            definition = input('\nВпишите ваше толкование: ')
            geek[term] = definition
            print('\nТермин', term, 'добавлен в словарь.')
        else:
            print('\nТакой термин уже есть! Попробуйте изменить его толкование.')
    elif choice == '3':
        term = input('Какой термин вы хотите переопределить?')
        if term in geek:
            definition = input('\nВпишите ваше толкование: ')
            geek[term] = definition
            print('\nТермин', term, 'переопределен.')
        else:
            print('\nТакого термина пока нет, попробуйте добавить его в словарь.')
    elif choice == '4':
        term = input('Какой термин вы хотите удалить?')
        if term in geek:
            del geek[term]
            print('\nТермин', term, 'удален.')
        else:
            print('\nНичем не могу помочь. Термина', term, ' нет в словаре.')
    else:
        print('Извините, в меню нет пункта', choice)

input('\n Нажмите Enter чтобы выйти')
print (geek.keys())
print (geek.values())
print (geek.items())