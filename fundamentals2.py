#print your name
#print("yasaswini")


#Create a Python script with both single-line and multi-line comments
person_name = "swaroop"
print(person_name)
#above code is written to print the name of the person

"""

To print a person name first we have to take a varaible 
and assign a value i.e a name which we want to display on the screen
now using the print statement the person name will be displed on the screen

"""

#Define a list containing three different data types.
list_1 = [7,"pandu",5.9]
print(list_1)

#Concatenate two strings and print the result
username_1 = input("enter the name1: ")
username_2 = input("enter the name2: ")
result = username_1 + username_2
print(result)

#Repeat a string three times and display the output
fruitname_1 = input("enter the fruitname1: ")
fruitname_2 = input("enter the fruitname2: ")
fruitname_3 = input("enter the fruitname3: ")
result = fruitname_1 + fruitname_2 + fruitname_3
print(result)

#Create a variable with a name that is a Python keyword
else = "yashu"
print(else)
#we shouldn not create a variable with a keyword because it displays the output as invalid

#Declare two variables, one storing an integer and the other a string
person_id = 464
person_name = "yasaswini"
print(person_id)
print(person_name)

#Convertion of float to an integer
percentage = 90.4
int_conversion = int(percentage)
print(int_conversion)
print(type(int_conversion))

#Convertion of an integer to a string
age = 23
str_conversion =str(age)
print(str_conversion)
print(type(str_conversion))

#Take the user's age as input and print a message using that input.
age = input("enter the age a person : ")
print(age)

#Write a program that prints a pattern using multiple print statements.
name_1 = "yasaswini"
name_2 = "ramya"
name_3 = "chandu"
print(name_1)
print(name_2)
print(name_3)

#a Python script for a simple task and adding comments to each step
num_1 = 23#assigned a value to the varaible
num_2 = 24#assigned a value to the variable
result = num_1 + num_2
print(result)
"""


to perform addition of numbers
first we have to take two variables and assign values to each variable 
use addition operator in between two varaibles 
lastly we have use print statement to display the result on the screen
 

"""

#Implement a program that uses a dictionary to store information about a book
book_information = {
    "title" : "little girls",
    "author" : "nithin" ,
    "publication year" : 2001
}
#print(book_information)

#Write a python program that takes a string as input 35 and return float value
id_information = "35"
float_conversion = float(id_information)
print(float_conversion)

#three Python keywords
#true,false
#used to represent boolean values
x = True
y = False
print(x and y)
 
#if ,else they are conditional statements which makes the decision based on the conditions

num_1 = 5
num_2 = 4
if num_1 > num_2 :
   print("true")
else :
   print("false")

#a script that swaps the values of two variables without using a temporary variable
person_1 = "ramya"
person_2 = "maggi"
person_1 , person_2 = person_2 , person_1
print("person_1 =" , person_1)
print("person_2 =" , person_2)

#a program that takes user input for their age, converts it to an integer and adding 5
person_age = input("age of a person is : ")
int_conversion = int(person_age)
print(int_conversion + 5 )

#calculator program that takes two numbers as input and performs arthematic operation
a = 2
b = 3
result = a + b , a - b , a * b
print(result)

#or 
num_1 = int(input("enter the number1 : "))
num_2 = int(input("enter the number2 : "))#result_add = num_1 + num_2
result_sub = num_1 - num_2
result_mul = num_1 * num_2
print("addition " , result_add)
print("subtraction " , result_sub)
print("multiplication" , result_mul)
























