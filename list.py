#What is the output of the following code?
#my_list = [10, 20, 30, 40, 50]
#print(my_list[1:4])
#a) [20, 30, 40]
#b) [10, 20, 30]
#c) [30, 40, 50]
#d) [20, 40, 50]
#answer = a

#Which method is used to add multiple elements to the end of a list?
#a) add()
#b) append()
#c) extend()
#d) insert()
#answer = c

#Consider the following list: fruits = ['apple', 'banana', 'orange']
#How can you remove 'banana' from the list?
#a) fruits.remove('banana')
#b) fruits.delete('banana')
#c) fruits.pop('banana')
#d) fruits.exclude('banana')
#answer = a

#What does the len() function return when applied to a list?
#a) The sum of all elements in the list
#b) The average of all elements in the list
#c) The number of elements in the list
#d) The maximum element in the list
#answer = c

#Which of the following list comprehensions generates a list of even numbers from 0 to 10?
#a) [x for x in range(11) if x % 2 == 0]
#b) [x for x in range(10) if x % 2 == 0]
#c) [x**2 for x in range(11)]
#d) [x**2 for x in range(10) if x % 2 == 0]
#answer = a


#Reverse List:
#Write Python code to reverse the order of elements in the given list my_list . Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)
#or
my_list = [10, 20, 30, 40, 50, 11]
print(my_list[::-1])

#Common Elements:
#Given two lists list1 and list2 , find and print the common elements between them.
empty_list = []
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
for i in list1 :
    if i in list2 :
        empty_list.append(i)
print(empty_list)
"""
to print the commmen elements from list1 and list2
first we have to create an empty list to store the common elements
then we  have use for loop and then list1 is assigned to i 
and now use if and memebership opeartor to know i elements are there in list 2 
then using append operator we add common elements to empty list
then using print statement we display the common elements in emptylist 

"""
#Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.
unique_list = []
original_list = [1, 2, 2, 3, 4, 4, 5]
for i in original_list:
    if i not in unique_list :
        unique_list.append(i)
print(unique_list)

#Remove duplicate elements from the given list duplicated_list and print the list without duplicates while preserving the order.
clean_list = []
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
for i in duplicated_list:
    if i not in clean_list :
        clean_list.append(i)
print(clean_list)


#List Concatenation
#Write a Python script that concatenates two lists and prints the result.
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = list1 + list2
print(result)

#List Repetition
#Write a Python script that repeats a list three times and prints the result.
my_list = [10,"yasaswini",4.9]
result = my_list * 3
print(result)

#list Removal
#Write a Python script that removes the elements at even indices from a list.
list = [1,2,3,4,5]
result = list[1::2]
print(result)

#List Insertion
#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list
list=[13,14,15]
list.insert(0, 10)
list.insert(1, 11)
list.insert(2, 12)
print(list)

#square Numbers Create a list of squares of numbers from 1 to 10.
print([x**2 for x in range(1,11)])

#even Numbers Generate a list of even numbers from 1 to 20
print([x for x in range(1,20)if x % 2 == 0])

#words Lengths Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"]
print([len(word)for word in words])
