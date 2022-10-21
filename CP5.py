lick = int(input('Введите число: '))
my = int(input('Введите систему счисления: '))
balls = ''
while lick>0:
    balls += str(lick%my)
    lick //= my
balls = balls[::-1]
print(balls)
