text = "qwer123tyuio4567"

# 1
count = 0
for letter in text:
    count += letter.isdigit()

print(count)


# 2
count = 0
i = 0
while i < len(text):
    letter = text[i]
    count += letter.isdigit()
    i += 1

print(count)