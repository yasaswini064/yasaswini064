#What is the main characteristic of Python strings?
#a) Mutable
#b) Immutable
#c) Dynamic
#d) Static
#answer = b

#How can you access the last character of a string in Python?
#a) my_string[-1]
#b) my_string[last]
#c) my_string[last_char]
#d) my_string(end)
#answer = a

#Which method is used to convert a string to uppercase in Python?
#a) to_upper()
#b) uppercase()
#c) .upper()
#d) case_upper()
#Answer = c

#What does the split() method do?
#a) Combines strings
#b) Splits a string into a list of substrings
#c) Finds a substring in a string
#d) Converts a string to lowercase
#Answer = b

#Which method is used to check if a string starts with a specific prefix?
#a) startswith()
#b) startwith()
#c) beginwith()
#d) initwith()
#answer = a

#You are given a string sentence . Print the characters at even indices.
#sentence = "Python is amazing"
#print(sentence[::2])

#You are given a string s . Replace all spaces in the string with underscores ( _ ) and print the modified string.
s = "Python is fun and powerful"
y = s.replace(" " , "_")
print(y)

#You are given a string s . Check if the string contains only digits.
s = "12345"
is_numeric = s.isdigit()
print(is_numeric)

#You are given a string s . Print the string in reverse order.
s = "Python is amazing"
print(s[::-1])

#You are given a string s . Capitalize the first letter of each word in the string and print the modified string
s = "python programming is fun"
capitalized_s= s.title()#The title() method automatically capitalizes the first letter of each word in a string.
print(capitalized_s)