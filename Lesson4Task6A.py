from itertools import count

for i in count(int(input('Введите  число начала итераций:  '))):
    print(i)
    qui = input()
    if qui == 'q' :
        break
