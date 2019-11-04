def hash(key):
....return len(key) % 13
storage = []
for i in range(13):
....storage.append([])
def get_value(key):
....index = hash(key)
....return storage[index]
def set_value(key, value):
....index = hash(key)
....storage[index].insert(0, value)
while True:
....command = input('Read, Write, Exit (r/w/e): ')
....print (command)
....if command == 'w':
........key = input('Ключ: ')
........value = input('Значение: ')
....if command == 'r':
........key = input('Ключ: ')
........print(get_value(key))
....if command == 'e':
        break
