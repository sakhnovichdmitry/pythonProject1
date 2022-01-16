# принимай - возвращай
# демонстрирует параметры и возвращаемые значения

# определение функций
# def display(message):
#     print(message*10)
# def give_me_five():
#     five = 375
#     return five
# def ask_yes_no(question):
#     """задает вопрос с ответом да/нет"""
#     response = None
#     while response not in ('y', 'n'):
#         response = input(question).lower()
#     return response
#
# # основная часть кода
# display('Вам сообщение.\n')
# number = give_me_five()
# print('Вот что возвратила функция give_me_five:', number)
# # answer = ask_yes_no('Пожалйста введите "y" или "n"')
# # print('Спасибо что ввели', answer)
# display('Бля\n')

# День рождения
# демонстрирует именнованные аргументы и значения параметров по умолчанию
#
# позиционные параметры
# def birthday1(name, age):
#     print('С днем рождения', name, '!', 'Вам сегодня исполняется', age, 'не так ли?\n')
#
# def birthday2(name = 'Товарищ Иванов', age = 1):
#     print('С днем рождения', name, '!', 'Вам сегодня исполняется', age, 'не так ли?\n')
# print(birthday2('Иван Иванович', 12))

# доступ отовсюду
# демонстрирует рабту с глобальными переменными
def read_global():
    print('В области виидимости функции read_global() значение value равно', value)
def shadow_global():
    value = -10
    print('В области виидимости функции shadow_global() значение value равно', value)
def change_global():
    global  value
    value = -10
    print('В области виидимости функции change_global() значение value равно', value)
# основная часть
# value глjбальная переменная, потому, что сейчас мы находимся в глобальной области видимости
value = 10
print('В глобальной области видимости значение переменной value сейчас стало равным', value, '\n')
read_global()
print('Вернемся в глобальную область видимости, здесь value по прежнему равно', value, '\n')
shadow_global()
print('Вернемся в глобальную область видимости, здесь value по прежнему равно', value, '\n')
change_global()
print('Вернемся в глобальную область видимости, значение value изменилось на', value, '\n')