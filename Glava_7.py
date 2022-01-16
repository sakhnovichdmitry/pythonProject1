# text_file = open('read_it.txt', 'r', encoding='utf-8')
# text_file.close()
#
# text_file = open('read_it.txt', 'r', encoding='utf-8')
# print(text_file)
# print(text_file.read(1))
# print(text_file.read(5))
# text_file.close()
#
# text_file = open('read_it.txt', 'r', encoding='utf-8')
# whole_thing = text_file.read()
# print(whole_thing)
# text_file.close()

# text_file = open('read_it.txt', 'r', encoding='utf-8')
# print(text_file.readline())
# print(text_file.readline())
# print(text_file.readline())
# text_file.close()

# text_file = open('read_it.txt', 'r', encoding='utf-8')
# lines = text_file.readlines()
# print(lines)
# print(len(lines))
# for line in lines:
#     print(line)
#
#
# text_file.close()
#
# text_file = open('read_it.txt', 'r', encoding='utf-8')
# for xyz in text_file:
#     print(xyz)
# text_file.close()

# text_file = open('read_it.txt', 'w', encoding='utf-8')
# text_file.write('Строка 1\n')
# text_file.write('Вторая строка\n')
# text_file.write('Третья, но самая важная строка\n')
# text_file.close()

# print('Создаю тектовый файл методом writelines().')
# text_file = open('test_file.txt', 'w', encoding='utf-8')
#
# lines = ['Строка 1\n', 'Строка два\n', 'Третья строка\n']
# text_file.writelines(lines)
# text_file.close()
# text_file = open('test_file.txt', 'r', encoding='utf-8')
# print(text_file.read())
# text_file.close()

# ЗАКОНСЕРВИРУЕМ
# import pickle, shelve
# print('Консервация списков.')
# variety = ['огурцы', 'помидоры', 'капуста']
# shape = ['целые', 'кубиками', 'соломкой']
# brand = ['Главпродукт', 'Чумак', 'Бондюэль']
# f = open('pickles1.dat', 'wb')
# pickle.dump(variety, f)
# pickle.dump(shape, f)
# pickle.dump(brand, f)
# f.close()
#
# print('Расконсервация списков.\n')
# f = open('pickles1.dat', 'rb')
# variety = pickle.load(f)
# shape = pickle.load(f)
# brand = pickle.load(f)
# print(variety)
# print(shape)
# print(brand)
# f.close()
#
# print('\nПомещение списков на полку')
# s = shelve.open('pickles2.dat')
# s['variety'] = ['огурцы', 'помидоры', 'капуста']
# s['shape'] = ['целые', 'кубиками', 'соломкой']
# s['brand'] = ['Главпродукт', 'Чумак', 'Бондюэль']
# s.sync()
# print('\nИзвлечение списков из файла полки:')
# print('Торговые марки - ', s['brand'])
# print('Формы - ', s['shape'])
# print('Виды овощей', s['variety'])
# s.close()

# ОБРАБОТАЕМ
# обработка исключительных ситуаций
try:
    num = float(input('Введите число:'))
except ValueError as e:
    print('Похоже это не число')
    print(e)