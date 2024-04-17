l = list("qwertyuiopasdfghjklzxcvbnm")

for index, element in enumerate(l):
    pos = index + 1
    if (pos % 3 == 0):
        print(element, pos)