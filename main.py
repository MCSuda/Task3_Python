num = int(input("Give me number: "))
listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listB = []
for x in listA:
    if x < num:
        listB.append(x)

print(listB)
