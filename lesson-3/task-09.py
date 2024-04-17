l = [1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7]

# 1
l_1 = l.copy()
for i in range(len(l_1)):
    while l_1.count(i) > 1:
        l_1.pop(i)

print(l_1)

# 2
l_2 = l.copy()
i = 0
 
while i < len(l_2):
    element = l_2[i]
    if l_2.count(element) > 1:
        del l_2[i+l_2[i:].index(element)]
    else:
        i += 1

print(l_2)