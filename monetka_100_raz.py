# Программа подбрасывает монетку 100 раз
# и сообщает сколько раз выпал орел и сколько решка

import random

i = 0
orel = 0
reshka = 0
monetka = random.randint(1, 2)

while i < 100:
    monetka = random.randint(1, 2)
    if monetka == 1:
        reshka += 1
    else:
        orel += 1
    i += 1

# else:
print("Орел", orel)
print("Решка", reshka)

input ("\n\nНажмите Enter, чтобы выйти")