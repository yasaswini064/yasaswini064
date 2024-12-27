#What is the value of result in the following code
#x = 15
#y = 4
#result = x // y
#print(result)
#result=3:option b

#What is the output of the following code?
#a = 7
#b = 3
#c = a % b
#print(c)
#result=1:option b

#Which assignment operator is equivalent to x = x * 5
#a) x **= 5
#b)x //= 5
#c)x *= 5
#d)x %= 5
#answer = c

#What is the result of the expression 5 < 3 or 2 == 2 ?
#a) True
#b) False
#c) Error
#d) None of the above
#answer = a

#If a = True and b = False , what is the value of not a or b ?
#a) True
#b) False
#c) Error
#d) None of the above
#answer = b


#Write a Python program to calculate the area of a rectangle using the given formula: area = length * width 
#rectangle_length = 10
#rectangle_width = 20
#area = rectangle_length * rectangle_width
#print(area)

#Write a Python program to demonstrate incrementing and decrementing a variable
#person_weight = 64
#person_weight += 10 #equivalent person_weight = +10
#print(person_weight)
#person_weight -= 5 #equivalent person_weight = -5
#print(person_weight)

#Write a Python program to convert temperature from Celsius to Fahrenheit.The formula for conversion is: F = (C * 9/5) + 32 
#celsius_temperature = 15
#fahrenheit_temparature = celsius_temperature * 9/5 + 32
#print(fahrenheit_temparature)

#Write a Python program to calculate the simple interest given the principal amount, rate, and time (in years)
#amount = int(input("enter the principal amount of loan taken : "))
#rate = int(input("annual interest (in %) : "))
#time = int(input("time taken to clear the loan (in years): "))
#simple_interest = amount * rate * time / 100
#print(f"simple_interest of a product is : {simple_interest}")

#A program to concatenate two strings.
#person_name = input("enter name of the person : ")
#person_surname = input("enter surname of a person : ")
#result = person_name + person_surname
#print(result)

#Write a Python program to convert a distance from kilometers to miles
#kilometer_distance = float(input("enter the distance travelled by a person in kilometers : "))
#formula mile = kilometer * 0.621371 
#1km approximately equals to 0.621371miles
#miles_distance = kilometer_distance * 0.621371
#print(f" to know the person covered the distance in miles is : {miles_distance} ")

#What do identity operators ( is and is not ) check in Python?
#a) Value equality
#b) Memory address identity
#c) Type equality
#d) Sequence membership
# anser = b

#Which of the following statements is correct for the identity operator is ?
#a) x is y is True if the values of x and y are equal.
#b) x is y is True if x and y refer to the same object.
#c) x is y is True if the type of x and y is the same.
#d) x is y is True if x and y are both None.
#answer = b

#what do membership operators ( in and not in ) check in Python?
#a) Memory address identity
#b) Type equality
#c) Value equality
#d) Sequence membership
#answer = d 

#which membership operator is used to check if a value is not present in a sequence?
#a) in
#b) not in
#answer = b

#program that takes user input for their name and age. Use formatted strings (f-strings) to print a message welcoming the user and stating their age
#user_name = input("enter the name of a person : ")
#user_age = input("enter the age of a person : ")
#print(f"the person's name is : {user_name} and his age is : {user_age}")

#script that defines a dictionary with information about a product (e.g., name, price, quantity)
#product_details = {
#   "name" : input("name of the product is : "),
#    "price" : input("price of the product is : "),
#   "quantity" : input("quantity of the product is : ")
#}
#print(f"The details of the product are:")
#print(f"Name: {product_details['name']}")
#print(f"Price: {product_details['price']}")
#print(f"Quantity: {product_details['quantity']}")
#to display the details of the product in dictionary type 
#first we have to declare a variable and then mention key pair values i.e name ,price, quantity of the product
#then using f strings print the detials of the product

#creating a list called numbers that contains integers from 1 to 10.
#Check if the number 5 is in the list.
#Check if the number 15 is not in the list.
list_numbers = [1,2,3,4,5,6,7,8,9,10]
print(5 is list)
print(15 is not list)