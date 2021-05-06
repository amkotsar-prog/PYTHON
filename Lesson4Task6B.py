from itertools import cycle

my_list = input('Введите список, разделяя элементы пробелом:  ').split()
ite = cycle(my_list)
qui = None

while qui != 'q':
    print(next(ite))
    qui = input()

