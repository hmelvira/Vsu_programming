def combsort(data):
    gap = len(data) # разрыв
    o = True # обмен
    while gap > 1 or o:
        gap = max(1, int(gap / 1.25))
        o = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i] 
                o = True 
    return data 
a = list(map(int, input().split())) 
print(combsort(a)) 
