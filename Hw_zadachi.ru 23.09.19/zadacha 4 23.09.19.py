n = list(input()) 
s = 0 
for i in range(0,len(n)): 
    if n[i] == '(': 
        s += 1 
    if n[i] == ')': 
        s -= 1 
if s == 0: 
    print ('Всё нормально') 
elif s <= 0: 
    print ('Не хватает ' + str(abs(s)) + ' открывающей(их) скобки(ок)!') 
elif s >= 0: 
    print ('Не хватает ' + str(s) + ' закрывающей(их) скобки(ок)!')
