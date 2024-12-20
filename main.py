numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_numbers = [x ** 2 for x in numbers if x % 2 == 0]

print(squared_even_numbers)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print(result)
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}

frequency_dict = {}

for value in test_dict.values():
    if value in frequency_dict:
        frequency_dict[value] += 1
    else:
        frequency_dict[value] = 1

print(frequency_dict)
