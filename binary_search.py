import random

def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = mid - 1
        else:
            low = mid + 1
        print(guess)
    return None

item = random.randint(0,1000)

print('Загаданное число -', item)

print('Промежуточные варианты:')
# def niochem(lst):
#     print(lst)


# spis = (1, 3, 5, 7, 9)

a = []
for i in range(1000):
    i += 1
    a.append(int(i))

# niochem(a)
#
# print(a)


print(binary_search(a, item))

