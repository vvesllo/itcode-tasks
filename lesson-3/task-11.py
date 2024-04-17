table = 'Пн Вт Ср Чт Пт Сб Вс\n'

for i in range((31 // 7) + 1):
    week = i
    for j in range(7*week, 7*(week + 1)):
        day = j + 1
        if (day > 31): break
        table += f"{day:<3}"
    table += '\n'

print(table)