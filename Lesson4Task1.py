from sys import argv
print(argv)


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
    except ValueError:
        time = float(input('Введите значение времени:  '))
        rate = float(input('Введите значение ставки:  '))
        bonus = float(input('Введите значение бонуса:  '))
    return time * rate + bonus

print(salary())
