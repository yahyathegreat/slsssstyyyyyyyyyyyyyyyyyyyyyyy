numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_numbers = [x ** 2 for x in numbers if x % 2 == 0]

print(squared_even_numbers)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print(result)
