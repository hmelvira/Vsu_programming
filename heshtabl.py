storage = [['Null']*19 for x in range(172)] # 19 т.к. AAA = 36; 172 т.к. zzz = 171)

def hash(key):
    s = 0
    for i in range(len(key)-1):
        s += ord(key[i]) - 65 # Т.к. буквы в ASCII начинаются с 65 ('A')
    s -= ord(key[len(key)-1]) - 65 # складываем коды первых букв и вычитаем код последней (для того чтобы разная последовательность одинаковых букв воспринималась как разные ключи)
    ind = (''.join(format(ord(x), 'b') for x in key)).count('0') # сумма 0 в 2-м представлении букв
    return s, ind

def get_value(key):
    index, index2 = hash(key)
    return storage[index][index2]

def set_value(key, value):
    index, index2 = hash(key)
    if storage[index][index2] == 'Null':
        storage[index][index2] = value
    else:
        previous = storage[index][index2]
        storage[index][index2] = value
        print('Значение '+str(previous)+' заменено на значение '+str(value)) # коллизия встречается крайне редко

def del_value(key):
    index, index2 = hash(key)
    value = storage[index][index2]
    storage[index][index2] = 'Null'
    qeturn str(value)

while True:
    command = input('Read, Write, Delete, Exit (r/w/d/e): ')
    if command == 'w':
        key = input('Ключ (состоит из 3 букв): ')
        value = input('Значение: ')
        set_value(key, value)
    if command == 'r':
        key = input('Ключ (состоит из 3 букв): ')
        print(get_value(key))
    if command == 'd':
        key = input('Ключ (состоит из 3 букв): ')
        print('Удалено значение: '+del_value(key))
    if command == 'e':
        break
