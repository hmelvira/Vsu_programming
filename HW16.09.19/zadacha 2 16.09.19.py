a, b, c, d, f = map(int,input().split()) 
if f != d: 
    print ((a * b - c) / (f - d)) 
else: 
    print('Делить на 0 нельзя!')
