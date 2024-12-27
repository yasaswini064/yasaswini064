#What is the output of the following code?
#my_dict = {'a': 1, 'b': 2, 'c': 3}
#print(len(my_dict))
#a) 1
#b) 2
#c) 3
#d) 4
#answer = c

#Which method is used to add a new key-value pair to a dictionary?
#a) add()
#b) insert()
#c) append()
#d) update()
#answer = d

#my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligudem'}
#How can you access the value associated with the key 'age'?
#a) my_dict.get('age')
#b) my_dict['age']
#c) my_dict.value('age')
#Dictionary Quiz: 2
#d) my_dict.retrieve('age')
#answer = b

#What happens if you try to access a key that doesn't exist in a dictionary using square brackets notation?
#a) It returns None.
#b) It raises a KeyError.
#c) It returns False.
#d) It adds the key to the dictionary.
#answer = b

#Which of the following methods returns a list of all the keys in a dictionary?
#a) keys()
#b) get_keys()
#c) all_keys()
#d) list_keys()
#answer = a

#Dictionary Update
my_dict = {'name': 'python', 'age': 25}
sample_dict = {
    'city' : '  we st godavari'
}
my_dict.update(sample_dict)
print(my_dict)

#Dictionary Access
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get('price'))
#or
print(product_info['price'])
 
#Dictionary Removal
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop('city')
print(my_dict)

#Dictionary Keys
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

#Dictionary Values
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())


#Write a Python script that updates a dictionary with a new key-value pair.
student_details = {'name' : 'yasaswini' , 'class' : 10 ,}
missing_details = {'rollnumber' : 464}
student_details.update(missing_details)
print(student_details)

#Write a Python script that accesses and prints the value associated with a specific key in a dictionary
users = {'user1' : 'swaroop','user2' : 'nithin', 'user3' : 'ramya'}
print(users.get('user1'))

#Write a Python script that removes a key-value pair from a dictionary.
aadhaar_numbers = {'person1' : 123456789123 , 'person2' : 987654321012 , 'person3' : 646463646660}
aadhaar_numbers.pop('person3')
print(aadhaar_numbers)

#Write a Python script that prints all the keys present in a dictionary.
fruits_prices = {'banana' : 20  , 'apple' : 50 , 'grapes' : 30}
print(fruits_prices.keys())

#Write a Python script that prints all the values present in a dictionary.
person_details = {'name' : 'venky' , 'qulaification' : 'mca' , 'age' : 24}
print(person_details.values())
