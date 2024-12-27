#What is the purpose of using functions in Python?
#a) To organize code into logical blocks
#b) To improve code readability and maintainability
#c) To enable code reuse
#d) All of the above
#answer =  d

#Which keyword is used to define a function in Python?
#a) def
#b) function
#c) define
#d) fun
#answer = a

#Which of the following is a valid way to call a function named my_function with no arguments in Python?
#a) my_function()
#b) call my_function()
#c) function my_function()
#d) my_function
#answer = a

#What is the scope of a variable defined inside a function in Python?
#a) Local scope
#b) Global scope
#c) Enclosing scope
#d) Built-in scope
#answer = a

#Write a Python function named add that takes two arguments a and b and returns their sum.
def add(a,b) :
    print(a+b)
add(10,20)

#Write a Python function named square that takes a number x as input and returns its square.
def square(x) :
    print(x**2)
square(4)

#Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
def factorial(n) :
    result = 1
    for i in range(1,n+1) :
       result *= i
    return result
n = int(input("enter a positive integer : "))
if n < 0 :
    print("factorial is not defined for negetive integer")
else :
    print(f"The factorial {n} is {factorial(n)} ")
    
#Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list
def list(my_list) :
    maximum = max(my_list)
    print(f"maximum value in the list :{maximum}")
numbers = [15,20,40,50,90]
list(numbers)

#Write a Python function named reverse that takes a string s as input and returns its reverse.
def character(my_name) :
    my_name = "yasaswini"
    print(my_name[::-1])
character("yasaswini")

#Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False .
def is_prime(numbers):
    if numbers<=1 :
        return False
    for i in range(2,numbers) :
        if numbers % i == 0:
            return False
    return True
numbers = int(input("enter the number :"))
print(is_prime(numbers))

#Fibonacci Function
#Write a Python function named fibonacci that takes a positive integer n as input and returns the n th Fibonacci number.
def fibonacci(n) :
    a,b= 0,1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a,b = b , a + b 
    return fib_series
n = int(input("enter the number of fibonacci numbers to generate: "))
print(fibonacci(n))

#Palindrome Function
#Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False .
def is_palindrome(my_word) :
    my_word = my_word.lower()
    if my_word ==my_word[::-1] :
        return True
    else :
        return False
my_word = str(input("enter the word : "))
print(is_palindrome(my_word))

#Sum of Squares Function
#Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.
def sum_of_squares(numbers) :
    sum = 0
    for num in numbers:
        result = num**2
        sum+= result
    return sum
numbers = [1,2,3,4,5,6,7,8]
print(sum_of_squares(numbers))

#Average Function
#Write a Python function named average that takes a list of numbers as input and returns the average value
def average(my_list):
    total = sum(my_list)  
    avg = total / len(my_list) 
    return avg  
numbers = [15, 20, 40, 50, 90]
print(f"Average value in the list: {average(numbers)}")




    

  
