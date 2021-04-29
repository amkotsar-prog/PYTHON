def fact(n):
    pr=1
    for i in range(1,n+1):
        pr = pr * i
        yield f' {i}! = {pr}'

for el in fact(int(input('Введите число факториала: '))):
        print(el)



