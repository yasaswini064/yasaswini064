#What does the break statement do?
#a) Skips the current iteration of a loop
#b) Exits the loop immediately
#c) Continues to the next iteration of a loop
#d) Does nothing
#answer : b

#When is the continue statement used?
#a) To exit a loop prematurely
#b) To skip the rest of the code for the current iteration and move to the next
#c) As a placeholder statement
#d) To iterate through a list
#answer : b

#What is the purpose of the pass statement?
#a) Exits a loop
#b) Skips the current iteration of a loop
#c) Acts as a null operation, doing nothing
#d) Skips the rest of the code for the current iteration
#answer : c

#Using break in a While Loop
#Write a Python program that takes a list of numbers as input numbers = [25, 30,20, 40, 15, 25] and prints the sum of the numbers.However, if the sum exceeds 100 stop adding numbers and print "Sum exceeded 100".
numbers = [25, 30, 20, 40, 15, 25]
sum = 0
i = 0
while sum <= 100 and i < len(numbers):
    sum += numbers[i]
    i += 1
    if sum > 100:
        print(f"Sum exceeded 100 , Current sum: {sum}")
        break
else:
    print(f"The total sum is {sum}")


"""

to calculate sum of the list first we have to assign a varaible to the list of numbers
the intialize sum = 0 and i = 0
then use while loop contion here we take i as index so we can know which number is list we are currently adding and len is used
to represent the length of the list so the index will only consider the numbers in this list only 
then if sum greater than 100 it displays sum exceeds 100 else it prints total sum

"""

##using continue in a For Loop
#Write a Python script that uses a for loop to iterate through numbers from 1 to 600. Print only the odd numbers, skipping the even ones using the continue statement.
for i in range (1,601) :
    if i % 2 == 0 :
        continue
    print(i)


#using pass in Conditional Statements
#Write a Python script that checks if a number is even or odd. If the number is even, print "Even"; if odd, do nothing (use the pass statement).
number = int(input("enter a number :"))
if number % 2 == 0 :
    print("number is even")
else :
    pass

"""

take a number as input 
then write if confition if number % 2 == 0 print number is even 
else if a number is odd then use pass to print nothing
pass represents null operation

"""

#Problem 4 Combining Transfer Statements
#Write a Python script that iterates through a list of words. If the word is "break," exit the loop using the break statement. If the word is "skip," skip the rest of the
#code for the current iteration using the continue statement. For any other word print the word.
list_words = ["start", "fast", "move","break", "stop", "skip",]

for word in list_words:
    if word == "break":
        break
    elif word == "skip":
        continue
    print(word)




    



    