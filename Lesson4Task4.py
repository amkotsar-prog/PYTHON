from random import randint

my_randlist = [randint(-10, 10) for _ in range(20)]
my_list = [el for el in my_randlist if my_randlist.count(el) == 1]
print(f'{my_randlist}\n {my_list}')
