import random

my_rand = [random.randint(0,1000) for i in list(range(0, random.randint(2,20)))]
my_list = [i for num, i in enumerate(my_rand[1:]) if i > my_rand[num]]

print (f'{my_rand}\n {my_list}')

