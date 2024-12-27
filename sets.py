#What is the output of the following code?
#my_set = {1, 2, 3, 4, 5}
#print(len(my_set))
#a) 1
#b) 5
#c) 4
#d) 0
#answer = b

#Which of the following methods is used to add an element to a set?
#a) add()
#b) insert()
#c) append()
#d) update()
#answer = a

#Consider the following sets:
#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}
#Which method would you use to find the elements that are common in both sets?
#a) intersection()
#b) union()
#c) difference()
#d) symmetric_difference()
#answer = a

#Which of the following statements about sets in Python is true?
#a) Sets are ordered collections of elements.
#b) Sets allow duplicate elements.
#c) Sets are mutable.
#d) Sets support indexing.
#answer = c

#Set Intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1=set1.intersection(set2)
print(set1)

#Set Union
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 = set1.union(set2)
print(set1)

#Set Difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 = set1.difference(set2)
print(set1)

#Set Symmetric Difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 = set1.symmetric_difference(set2)
print(set1)

#Set Membership Test
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

#Write a Python script that finds and prints the intersection of two sets.
set_1 = {5, 10, 15, 20, 25}
set_2 = {15, 20, 25, 30, 35}
set_1=set_1.intersection(set_2)
print(set_1)

#Write a Python script that finds and prints the union of two sets.
set1 = {'ramya', 28, 5.7}
set2 = {'narayana', 33, 5.9}
set1 = set1.union(set2)
print(set1)

#Write a Python script that finds and prints the difference between two sets.
set_yashu = {23, 4.9, 2001}
set_gnana = {23, 5.1, 2001}
set_yashu = set_yashu.difference(set_gnana)
print(set_yashu)

#Write a Python script that finds and prints the symmetric difference between two sets.
set1 = {'yashu','swaroop', 'ramya', 'maggi', 'nithin'}
set2 = {'pandu', 'yashu', 'swaroop', 'bhavana', 'chandu'}
set1 = set1.symmetric_difference(set2)
print(set1)