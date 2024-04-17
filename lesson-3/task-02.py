text = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
words = text.split()
words_length = len(words)

# 1
longest_word = ''
max_length = 0
for word in words:
    if (len(word) > max_length):
        max_length = len(word)
        longest_word = word

print(longest_word)

# 2
longest_word = ''
max_length = 0
i = 0
while i < words_length:
    word = words[i]
    if (len(word) > max_length):
        max_length = len(word)
        longest_word = word
    i += 1

print(longest_word)
