import math

def cria_lista ():
    total = input().split(" ")
    return total
    
total1 = cria_lista()
total2 = cria_lista()

x1 = float (total1[0])
y1 = float (total1[1])
x2 = float (total2[0])
y2 = float (total2[1])

distancia = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

print('{:.4f}'.format(distancia))




