    
n = list(input()) 
k = int(input()) 
a = [] 
for i in range(0,len(n)): 
if ord(n[i])>=48 and ord(n[i])<= 57: 
a.append(n[i]) 
print(str(k) + '-ая цифра в строке ' + str(a[k-1]))
