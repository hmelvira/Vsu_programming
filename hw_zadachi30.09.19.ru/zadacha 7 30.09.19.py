text = str(input()) 
print ('Самое длинное: ' + sorted(text.split() ,key=len).pop()) 
mcount = 0 
n = text.split() 
for i in range(0, len(n)): 
    if n.count(n[i]) > mcount: 
        mcount = n.count(n[i]) 
        m = n[i] 
print ('Самое частое: ' + m) 
