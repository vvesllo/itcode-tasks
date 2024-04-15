a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

c = a + b
c_sorted = sorted(c)
c_no_dup = list(set(c_sorted))

print(c_sorted)
print(c_no_dup)