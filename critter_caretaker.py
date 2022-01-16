# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "счастлив"
        elif 5 <= unhappiness <= 10:
            m = "в порядке"
        elif 11 <= unhappiness <= 15:
            m = "ужасно"
        else:
            #m = "помер"
            print('Ваш питомец помер, сорян')

        return m

    def talk(self):
        print("Я", self.name, "чуствую себя", self.mood, "сейчас.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Ням")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('уиииии')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как назовем питомца?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print\
            ("""
        Мой питомец

        0 - Выход
        1 - Спросить питомца
        2 - Покормить питомца
        3 - Поиграть с питомцем
        """)

        choice = input("Выбор: ")
        print()

        # exit
        if choice == "0":
            print("пака")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nТы тупой(ая) потому что", choice, "не правильно")


main()
("\n\nPress the enter key to exit.")
