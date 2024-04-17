l = [1, 2, 3, 4, 4, 5]

for i in l:
    if (l.count(i) > 1):
        print("Список содержит дубликаты")
        break
else:
    print("Список не содержит дубликаты")