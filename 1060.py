cont = 0
val = 1
while val <= 6:
    num = float(input())
    if num > 0:
        cont += 1
    val += 1
print(cont, "valores positivos")