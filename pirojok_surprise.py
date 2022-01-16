# Пирожок с сюрпризом
# При запуске выводит один из 5 случайных сюрпризов

import random

surprize = random.randint(1, 5)

if surprize == 1:
    print ("Вы получаете нихуя")
elif surprize == 2:
    print("Вы получаете пончик")
elif surprize == 3:
    print("Вы получаете сырник")
elif surprize == 4:
    print("Вы получаете пиздюлей")
else:
    print("Вы получаете 100 баксов")