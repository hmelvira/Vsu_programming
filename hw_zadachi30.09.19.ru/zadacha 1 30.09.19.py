n = list(input())
a = ''
b = ''
z = ''
c = 0
d = 0
for i in range(0,len(n)):
    if ord(n[i])>=48 and ord(n[i])<= 57:
        b += n[i]
    elif n[i] == '.':
        b += n[i]
    elif n[i] == '+':
        a = b
        b = ''
        z = '+'
    elif n[i] == '-':
        a = b
        b = ''
        z = '-'
    elif n[i] == '/' and n[i+1] == '/' and d == 0:
        a = b
        b = ''
        z = '//'
        d = 1
    elif n[i] == '*' and n[i+1] == '*' and d == 0:
        a = b
        b = ''
        z = '**'
        d = 1
    elif n[i] == '*' and d == 0:
        a = b
        b = ''
        z = '*'
        d = 1
    elif n[i] == '/' and d == 0:
        a = b
        b = ''
        z = '/'
        d = 1
    elif n[i] == '%':
        a = b
        b = ''
        z = '%'
    if i == len(n)-1:
        if z == '+':
            c = float(a) + float(b)
        if z == '-':
            c = float(a) - float(b)
        if z == '*':
            c = float(a) * float(b)
        if z == '/':
            c = float(a) / float(b)
        if z == '//':
            c = float(a) // float(b)
        if z == '**':
            c = float(a) ** float(b)
        if z == '%':
            c = float(a) / 100 * float(b)
print (str(round(c, 1)))
