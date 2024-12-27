#What does the all() function return when applied to an empty tuple?
#A True
#B False
#C Error
#answer =  A
 
#Which of the following statements correctly creates a tuple?
#A my_tuple = [1, 2, 3]
#B my_tuple = (1, 2, 3)
#C my_tuple = {1, 2, 3}
#answer =  B

#What is the output of the following code snippet?
#my_tuple = (1, 2, 3)
#print(len(my_tuple))
#A 1
#B 2
#C 3
#anmswer = C

#Which of the following statements about tuples in Python is true?
#A Tuples are mutable.
#B Tuples can only store elements of the same data type.
#C Tuples use square brackets [] for declaration.
#answer = A

#write a program that creates a tuple containing three elements: your name, your age, and your favorite color. Then print the tuple
my_details = ('yasaswini', 23, 'black')
print(my_details)

#Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.
days_of_the_week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print(days_of_the_week[2])

#tuple concatenation
odd_numbers = (1,3,5,7,9)
even_numbers = (2,4,6,8,10)
result = odd_numbers + even_numbers
print(result)


#tuple Unpacking
dimensions_of_rectangle = ('length' , 'width')
length ,width = dimensions_of_rectangle
rectangle_length = int(input("enter the length of the rectangle : ")) 
rectangle_width = int(input("entyer the width of the recatngle : "))
area_of_the_rectangle = rectangle_length * rectangle_width
print(area_of_the_rectangle)

#write a program that checks if a given element exists in a tuple.
id_numbers = (24,63,54,89,20)
print(54 in id_numbers)

#Write a Python program to generate a bill for a supermarket purchase.
# List of items and their prices
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print("Item    Price")
print("--------------")
total_cost = 0
for item, price in items:
    print(f"{item}  {price:.2f}")
    #f"{item} {price:.2f}" prints the item's name and price, formatted to two decimal places for clarity.
    total_cost += price
print("--------------")
print(f"Total  {total_cost:.2f}")

    





