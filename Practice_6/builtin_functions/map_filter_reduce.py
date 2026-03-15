from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x*x, numbers))
print("Squares using map:", squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

total_sum = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", total_sum)

string_numbers = ["10", "20", "30"]
converted = list(map(int, string_numbers))
print("Converted to int:", converted)

print("Type of numbers:", type(numbers))
print("Type of squares:", type(squares))