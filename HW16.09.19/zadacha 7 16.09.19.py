x, y = map(int,input().split()) 
s = 0 
if x > y: 
    x, y = y, x 
for i in range(x,y+1,1): 
    if i % 5 == 0: 
        s += 1 
print (s)
