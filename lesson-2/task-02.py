text = input("Enter text: ")

h_1 = text.find('h')
h_2 = text.rfind('h')
new_text = text[:h_1+1] + text[h_1+1:h_2].replace('h', 'H') + text[h_2:]
print(new_text)