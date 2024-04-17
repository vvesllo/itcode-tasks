n = 10
table = ""

for i in range(1, n+1):
    table += f'{i:5}'
    for j in range(2, n+1):
        table += f"{(i*j):5}"

    table += '\n'


print(table)