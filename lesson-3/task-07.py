string_1 = "hello"
string_2 = "deified"

# 1
if string_1 == string_1[::-1]:
    print(f"Строка `{string_1}` - палиндром")
else:
    print(f"Строка `{string_1}` - не палиндром")


# 2
string_len = len(string_2)
for i in range(string_len // 2):
    if (string_2[i] != string_2[string_len - (i + 1)]):
        print(f"Строка `{string_2}` - не палиндром")
        break
else:
    print(f"Строка `{string_2}` - палиндром")

