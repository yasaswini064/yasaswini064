#What is the purpose of the map() function in Python?
#a) To filter elements from an iterable
#b) To apply a function to each element of an iterable
#c) To reduce an iterable to a single value
#d) To sort elements of an iterable
#answer = b

#Which of the following functions is NOT a part of the functools module?
#a)map()
#b)filter()
#c)reduce()
#d)partial()
#answer = a

#What does the filter() function do?
#a) Applies a function to each element of an iterable
#b) Reduces an iterable to a single value
#c) Filters elements from an iterable based on a condition
#d) Sorts elements of an iterable
#answer = c

#Python, what is the purpose of the reduce() function?
#a) To apply a function to each element of an iterable
#b) To filter elements from an iterable
#c) To concatenate strings or join lists
#d) To apply a function to pairs of elements in an iterable until it's reduced to a single value
#answer = d

#Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the map() function with a lambda function to implement this.
obj = map(lambda i : i**2,[1,2,3,4,5,6,7,8,9])
print(list(obj))

#Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. Use the filter() function with a lambda function to implement this
obj = filter(lambda i : i >= 0 , [-1,2,4,5,6,8,-3,-5])
print(list(obj))

#Write a Python function calculate_factorial(n) that calculates the factorial of a given number n . Use the reduce() function with an appropriate lambda function to implement this.

from functools import reduce
def calculate_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(calculate_factorial(3))

#Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() function with an appropriate lambda function to implement this.

from functools import reduce
def count_vowels(string):
    return reduce(lambda count, char: count + (char in "aeiouAEIOU"), string, 0)
print(count_vowels("Are you okay ?"))

