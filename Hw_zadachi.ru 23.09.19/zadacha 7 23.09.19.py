from random import randint 
n = randint(0, 100) 
while True: 
    s = int(input()) 
    if s > n: 
        print('Загаданное число меньше!') 
    if s < n: 
        print('Загаданное число больше!') 
    if s == n: 
        print('Вы угадали число!') 
        break
