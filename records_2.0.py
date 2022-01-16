# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None

while choice != '0':
    print(
    '''
    Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    '''
    )
    choice = input('Ваш выбор: ')
    print()
# выход
    if choice == '0':
        print('До свидания')
# вывод лучших результатов на экран
    elif choice == '1':
        print('Рекорды\n')
        print('ИМЯ\tРЕЗУЛЬТАТ')
        for entry in scores:
            score, name = entry
            print(name, '\t', score)
# добавляем очки
    elif choice == '2':
        name = input('Впишите имя игрока: ')
        score = int(input('Впишите его результат: '))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #В списке остается только 5 рекордов
    else:
        print('Извините, в меню нет пункта', choice)

input('\n Нажмите Enter чтобы выйти')