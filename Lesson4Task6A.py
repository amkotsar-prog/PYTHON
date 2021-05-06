from itertools import count

for i in count(int(input('Введите  число начала итераций:  '))):
    print(i)
    qui = input()
    if qui == 'q' :
        break



# a = int(input('Введите число начала итераций:  '))
# for el in count(a):
    # print(el)

"""list_b = split(input('Введите значения списка для перебора: '))
iter = cycle(list_b)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))"""
