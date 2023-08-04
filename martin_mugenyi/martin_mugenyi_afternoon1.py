# Dictionary is used to store data valuesin key value pairs
# Dictionary is ordered and doesn't allow duplicates
# Dicts can have items of any datatype
my_dict = {
    'phone':'iphone',
    'iphone_model': 'iphone15',
    'year': 2023
}

print(my_dict)

# Length of a dictionary
print(len(my_dict))

# Data type
print(type(my_dict))

# Accessing Dictionary items
print(my_dict['phone'])

y =my_dict.get("year")
print(y)

z = my_dict.keys()
print(z)


print(my_dict.items())

# Exercise 1: Use the values() method to return a list of all values in the dictionary 
# Ex 2: check if a key does exist in a dictionary
# Ex 3: how to change dictionary items,  how to update
# Ex 4: how to add dictionary items , how to remove dictionary items
#Ex 5: how to loop through a dictionary and how to nest dictionaries
print('---------Exercise 1 dictionary---------')
print(my_dict.values())

print('---------Exercise 1 dictionary---------')
if 'phone' in my_dict:
    print("The key 'phone' exists in the dictionary")
else:
    print("This key does not exist in the dictionary")

print('---------Exercise 3 dictionary---------')
my_dict['year'] = 2024
print(my_dict)
print('using update method')
my_dict.update({"phone_model": "iphone16"})
print(my_dict)

print('---------Exercise 4 dictionary---------')
my_dict["color"] = "red"
my_dict.update({"RAM": "12GB"})
print(my_dict)

print("Removing dict items using various mthods")
my_dict.pop("color")
print(my_dict)

del my_dict["RAM"]
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print(my_dict)

print('---------Exercise 5 dictionary---------')
my_dict1 = {
    'phone':'iphone',
    'iphone_model': 'iphone15',
    'year': 2023
}
for x,y in my_dict1.items():
    print(x, y)

for x in my_dict1.keys():
    print(x)

for x in my_dict1.values():
    print(x)

for x in my_dict1:
    print(my_dict1[x])

print("Nested dictionary")
child1 = {
    "name": "Isaac",
    "year": 2000
}

child2 = {
    "name": "Peter",
    "year": 2004
}

child3 = {
    "name": "Larry",
    "year": 2001
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(my_family["child2"]["name"])
print(my_family["child1"]["name"])
print(my_family["child3"]["name"])
print(my_family)
# Numbers
# integer, floats, complex

w = 10 # int
r = 3.9 # float
s = 2j # complex

print(type(w))
print(type(r))
print(type(s))

# Integers
a = 2
b = 32682731919
c = - 567889283
print(type(a))
print(type(b))
print(type(c))

# Floats
g = 2.45
z = 3.6
e = -2.40432

print(type(g))
print(type(z))
print(type(e))

# Complex numbers

h = 5 + 10j
t = 4j
x = -2j

print(type(h))
print(type(t))
print(type(x))

# convert from int to complex
p = complex(w)
print(p)
print(type(p))

# convert from int to float
o = float(a)
print(o)
print(type(o))

# convert from float to complex
f = complex(z)
print(f)
print(type(f))

# convert from complex to float
# c = float(t)
# print(c)
# print(type(c)) # Note: we can't convert a complex number to any other type of number
print("Note: we can't convert a complex number to any other type of number")

# type casting 
# Works mostly when you want to specify a variable type

h = int(20)
y = int(30000000000000)
a = int("8")

print(h)
print(y)
print(a)

# Strings
print('Afternoon')
print("Afternoon")

w_z = "Afternoon"
print(w_z)

# Multiline string
print(
 """
      I am offering BSSE Year Three
    Currently doing recess in python,
    Data science, Django.
"""
)

# string arrays
e = "Morning"
print(e[5])

# exercise
# use len()
# for loop in a string
# slicing in strings

print('----------Exercise 1 use len() on a string--------')
print(len(e))

print('----------Exercise 2 use of for loop in a string--------')
for char in range(0, len(e)):
    print(e[char])

print('----------Exercise 3 slicing in strings--------')
print(e[2:5])
print(e[:5])
print(e[2:])
print(e[-5:-2])
# how to modify string
print(e.lower())
print(e.upper())

# remove white space
m = " Afternoon "
print(m.strip())

# string concatenation
k = "class"
l = "room"
print(k+l)

# string formatting 
#The format() takes the passed parameters, formats them and places
# them in the string where the placeholders {} are
age = 21
name = "My name is martin and I'm {}"
print(name.format(age))

# boolean
print(20 < 10)
print(30 == 30)
print(15 > 21)

print(bool(10))

# exercise
# Use condition to show how to use booleans 
print('-----------Exercise about booleans---------')

if(3 < 0):
    print(3 < 0)
else:
    print("False")

if(3 > 0):
    print(3 > 0)
else:
    print("False")

if(4 % 2 == 0  ):
    print(4 % 2 == 0 ,":4 is divisable by 2")