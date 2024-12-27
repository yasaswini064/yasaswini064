#What is the purpose of the for loop in Python?
#a) To check a condition and execute a block of code if it's true.
#b) To repeatedly execute a block of code for each element in a sequence.
#c) To perform arithmetic operations.
#d) To define a function.
#answer : b

#How do you iterate over a range of numbers in a for loop?
#a) Using the enumerate() function.
#b) Using the range() function.
#c) Using the while loop.
#d) Using the list() function.
#answer : b

#When does a while loop stop executing?
#a) When the loop variable reaches the end of the sequence.
#b) When the loop condition becomes false.
#c) When the loop variable is equal to a specific value.
#d) When the loop is explicitly terminated using break .
#answer : b , d

#what does the while loop syntax look like in Python?
#a)for variable in iterable:
#b)while condition:
#c)if condition:
#d)loop while condition
#answer : b

#Sum of Squares using for loop
sum = 0
for i in range(1,6) :
    result = i ** 2
    sum += result
    print(sum)

#Countdown using while loop 
count = 5 
while count >= 1:  
    print(count)  
    count -= 1

#Multiplication Table with Nested For Loop
number = int(input("enter the number : "))
for i in range (1,2) :
    for j in range(1,11) :
        print(f"{number} * {j} = {number * j}")

#Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive)
sum = 0
for i in range(0, 11, 2):  # Loop from 0 to 10, stepping by 2 (even numbers)
    sum += i              # Add the current even number to the sum
print(sum)
   
#Calculate the sum of all numbers from 1 to a given number
sum = 0
number = int(input("enter the number : "))
for i in range (1,number+1) : #add 1 to the number to include the number
    sum+= i#now add current number to the sum
print(sum) #print used to display the sum of numbers

#Display numbers from a list using loop
list_1 = [2,4,6,8,20]
for i in list_1:
    print(i)

#Display numbers from -10 to -1 using for loop
for i in range(-10,0) :
    print(i)

#Write a program to display all prime numbers within a range
starting_num = int(input("enter a starting number :"))
ending_num = int(input("enter ending number : "))
for num in range(starting_num, ending_num + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is prime")



     

    



    