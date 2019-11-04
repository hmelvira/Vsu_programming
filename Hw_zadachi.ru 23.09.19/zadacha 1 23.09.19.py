n = [] 
while True: 
    s = input() 
    if s == '': 
        break 
    n.append(s) 
print (','.join(str(n[i]) for i in range(0, len(n))))
