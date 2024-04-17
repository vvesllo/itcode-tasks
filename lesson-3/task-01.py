n = 10
# 1
result = 0
for i in range(n):
    if (i % 2 == 0):
        result += i
    
print(result)

# 2
result = 0
i = 0
while i < n:
    if (i % 2 == 0):
        result += i
    i += 1
    
print(result)