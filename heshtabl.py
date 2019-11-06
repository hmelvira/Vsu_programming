storage = [['Null']*31 for x in range(2049)]

def hash(key):
    s = 0
    index2 = (''.join(format(ord(x), 'b') for x in key)).count('0') # сумма 0 в 2-м представлении ключа
    index = ''.join('0'+format(ord(x), 'b') for x in key)
    for i in range(2):
        index = linetokey(index)
    index = int(index, 2) » 1 # перевод из 2 системы в 10 и побитовый сдвиг вправо для уменьшения значения
    return index, index2

def linetokey(line):
    part1, part2 = map(''.join, zip(*[iter(line)]*(len(line)//2)))
    key = ''
    if part1 == part2:
        key = part1 # т.к. XOR выдаст 000...0
    else:
        lpart1 = list(map(int,part1))
        lpart2 = list(map(int,part2))
        for i in range(len(lpart1)):
            key += str(lpart1[i] ^ lpart2[i]) # XOR
    return key

def get_value(key):
    index, index2 = hash(key)
    return storage[index][index2]

def set_value(key, value):
    index, index2 = hash(key)
    if storage[index][index2] == 'Null':
        storage[index][index2] = value
    else:
        print('Значение '+str(storage[index][index2])+' заменено на значение '+str(value))
        storage[index][index2] = value

def del_value(key):
    index, index2 = hash(key)
    value = storage[index][index2]
    storage[index][index2] = 'Null'
    return str(value)

while True:
    command = input('Read, Write, Delete, Exit (r/w/d/e): ')
    if command == 'w':
        key = input('Введите ключ (максимум 6 символов): ')
        value = input('Введите значение: ')
        set_value(key, value)
    if command == 'r':
        key = input('Введите ключ (максимум 6 символов): ')
        print('Значение: '+str(get_value(key)))
    if command == 'd':
        key = input('Введите ключ (максимум 6 символов): ')
        print('Удалено значение: '+del_value(key))
    if command == 'e':
        break 
