numbers = '1,2,3,4,5,6'

numbers_map = map(int, numbers.split(','))

numbers_tuple = tuple(numbers_map)
numbers_list = list(numbers_map)

print(numbers_tuple)
print(numbers_list)