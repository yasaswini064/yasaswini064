#Indentation is crucial in Python to:
#A. Improve code readability
#B. Indicate the end of the program
#C. Separate code blocks
#D. Define the scope of a code block
#answer : d

#x = 10
#if x > 5:
#print("Greater than 5")
#else:
#print("5 or less")
#A. Greater than 5
#B. 5 or less
#C. Both A and B
#D. None of the above
#answer = a

#if the if-elif-else statement, how many conditions can be checked?
#A. Only one
#B. Two
#C. Multiple
#D. None
#answer = c

#what is the purpose of the else statement in Python?
#A. To handle errors
#B. To provide an alternative block of code when the if condition is false
#C. To terminate the program
#D. To declare variables
#answer = b

#Which of the following statements is true about a nested if statement?
#A. It is not allowed in Python
#B. It allows for more complex conditional logic
#C. It always leads to syntax errors
#D. It can only contain one level of nesting
#answer = b

#Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.

letters = input("enter letters : ")

vowels = "a,i,e,o,u"

if letters in vowels : 
    print("letters is vowels : ")

else :
    print("letters is not vowels : ")

#age group classification
age = int(input("enter age of person : "))
if age <= 12 :
    print("person is a child")
elif age <= 17 :
    print("person is a teeneger")
elif age <= 64 :
    print("person is a adult") 
else :
   print("person is senior")


#number classifier

number = int(input("nter a number : "))
if number < 0 :
    print("number is negetive")
elif number == 0 :
    print("number is zero")
else :
    print("number is positive")

#leap Year Checker
year = int(input("enter a year : "))
if (year %4 == 0 and year %100 != 0) or (year %400 == 0) :
    print(f"{year}year is a leap year")
else : 
    print(f"{year}year is not a leap year")

#calculator
num_1 = int(input("enter number1 : "))
num_2 = int(input("enter number2 : "))
result_add = num_1 + num_2
result_mul = num_1 * num_2
result_sub = num_1 - num_2
result_div = num_1 / num_2
print(result_add)
print(result_sub)
print(result_mul)
print(result_div) 

#short hand if
x = 8
print(f"x is even {x}")if x % 2 == 0 else print(f"result is odd {x}")

#discount Calculator
original_price = float(input("enter the orinal price : "))
discount_percentage = float(input("enter the dicount percentage : "))
discount_percentage = discount_percentage / 100 * original_price 
final_price = original_price - discount_percentage
print(final_price)

#BMI Calculator
person_weight = float(input("enter the weight of a person : "))
person_height = float(input("enter the height of a person : "))
body_mass_index = (person_weight) / (person_height) ** 2
print(body_mass_index)

