text = "Hello world"

result = ''
for i in range(len(text), 0, -1):
    result += text[i-1]

print(result)