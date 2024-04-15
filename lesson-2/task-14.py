array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]

m = 5
n = 5

array_T = [[] for _ in range(n)]

for i in range(m):
    for j in range(n):
        array_T[j].append(array[i][j])

print(array_T)