n = list(map(str,input().split())) 
m = [] 
while len(n) > 0: 
    if len (n) > 0: 
        m.append ([n[0], n.count(n[0])]) 
        x = n[0] 
        while n.count(x) > 0: 
            n.remove(x) 
        else: 
            break 
            print ('\n'.join(m[i][0]+' | '+str(m[i][1]) for i in range (0,len(m))))
