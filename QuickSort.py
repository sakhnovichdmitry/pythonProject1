import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]
# блок для визуализации работы алгоритма
        # print('Длина списка на этом шаге - ', len(array))
        # print('меньше опорного значения - ', less)
        # print('опорное значение - ', pivot)
        # print('больше опорного значения - ', greater)
        # print()
        # input('Нажмите что нибудь')

        return quicksort(less) + [pivot] + quicksort(greater)

#
# a = [10, 5, 2, 4, 5, 2, 7]

a = []
for i in range(10):
   a.append(random.randint(0, 50))

print('список без сортировки', a)
print('отсортированный список', quicksort(a))



