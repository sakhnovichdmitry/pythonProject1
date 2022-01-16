#Отгадай число
#
# Компьютер выбирает число в диапазоне от 1 до 100
# Игрок пытается отгадать это число, и компьютер говорит,
# предположение больше/меньше, чем загаданное число,
# или попало в точку

def ask_number(question, low, high):
    """просит ввести число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
def main():
    import random

    print("\tДобро пожаловать в игру 'Отгадай число'!")
    print("\nЯ загадал натуральное число от 1 до 100.")
    print("Постарайтесь отгадать его за минимальное число попыток")

    # Начальные значения
    the_number = random.randint(1, 100)
    # guess = int(input("Ваше предположение: "))
    guess = ask_number('Ваше предположение:', 1, 100)
    tries = 1

    #Цикл отгадывания
    while guess != the_number:
        if guess > the_number:
            print("Меньше...")
        else:
            print("Больше...")
        # guess = int(input("Ваше предположение: "))
        guess = ask_number('Ваше предположение:', 1, 100)
        tries += 1

    print("Вам удалось отгадать число! Это и в самом деле", the_number)
    print("Вы затратили на угадываение всего лишь ", tries, "попыток!\n")
main()
input ("\n\nНажмите Enter, чтобы выйти")

