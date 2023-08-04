print('----------------Lists-----------------')
# Ex 1.1
my_list = ['Martin','Ritah','Larry','Peter','Robert']
print(my_list[1])

# Ex 1.2
my_list[0]= "Paul"
print(my_list)
# Ex 1.3
my_list.append("Max")
print(my_list)
# Ex 1.4
my_list.insert(2, "Bathel")
print(my_list)
# Ex 1.5
my_list.pop(3)
print(my_list)
# Ex 1.6
print(my_list[-1])
# Ex 1.7
names = ['Martin','Ritah','Larry','Peter','Robert','Passy','Daina']
for index in range(0, 6):
    if(index == 2 or index == 3 or index == 4):
        print(names[index])

# Ex 1.8
countries = ['Uganda', 'Kenya', 'Tanzania', 'Rwanda','Burundi']
East_Africa = []

East_Africa = countries.copy()
print(East_Africa)
# Ex 1.9
for country in range(0,len(East_Africa)):
    print(East_Africa[country])

# Ex 1.10
animals = ['lion','tiger', 'antelope','monkey', 'snake']
animals.sort()
print(animals)
animals.sort(reverse = True)
print(animals)
# Ex 1.11
for item in animals:
    if item.startswith('a'):
        print(item)
# Ex 1.12
surnames = ['Mugenyi', 'Makula', 'Kibalama']
first_names = ['Martin', 'Joshua','Moris']

name = surnames + first_names
print(name)


print('-------------Tuples-------------------')
# Ex 2.1
x  = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print(favorite_brand)
# Ex 2.2
m = x[-2]
print(m)
# Ex 2.3
y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)
# Ex 2.4
y = list(x)
y.append("Huawei")
x = tuple(y)
print(x)
# Ex 2.5
for item in x:
    print(item)
# Ex 2.6
y = list(x)
y.pop(0)
x = tuple(y)
print(x)
# Ex 2.7
cities = ['Kampala', 'Mbarara','Gulu','Lira']
tuple_of_cities = tuple(cities)
print(tuple_of_cities)
# Ex 2.8
(city_1, city_2, city_3, city_4) = x 
print(city_1)
print(city_2)
print(city_3)
print(city_4)
# Ex 2.9
for index in range(0, len(tuple_of_cities)):
    if(index == 1 or index == 2 or index == 3):
        print(tuple_of_cities[index])

# Ex 2.10
second_name_tuple = ('Mugenyi', 'Makula', 'Kibalama')
first_name_tuple = ('Martin', 'Joshua','Moris')

names_tuple = second_name_tuple + first_name_tuple
print(names_tuple)
# Ex 2.11
color = ('red','orange','blue')
multiplied_colors = color * 3
print(multiplied_colors)
# Ex 2.12
thistuple = (1,3,7,8,7,5,4,6,8,5)
number_of_times_8_appears_in_the_tuple = thistuple.count(8)
print("8 appears: ",number_of_times_8_appears_in_the_tuple, "times")

print('------------------Sets------------------------')
# Ex 3.1
drinks = ['nile','guinness','bell']
alcohol_set = set(drinks)
print(alcohol_set)
# Ex 3.2
alcohol_set.add('tusker')
alcohol_set.add('tequila')
print(alcohol_set)
# Ex 3.3
mySet = {'oven', 'kettle', 'microwave', 'refrigerator'}
if 'microwave' in mySet:
    print('microwave' in mySet, ":Microwave does exist in the list")
# Ex 3.4
mySet.remove('kettle')
print(mySet)

# Ex 3.5
for item in mySet:
    print(item)

# Ex 3.6
set_1 = {'pen','book','chalk','calculator'}
list_1 = ['teacher', 'student']
set_2 = set(list_1)
set_1.update(set_2)
print(set_1)

# Ex 3.7
age_set = {23, 45, 56}
name_set = {"Danny",'Larry', "Sevo"}
new_set = name_set.union(age_set)
print(new_set)

print("--------------------Strings--------------------")
# Ex 4.1
age = 21
name = "My name is Martin and I'm {}"
print(name.format(age))

#Ex 4.2
txt = " Hello, Uganda!  "
print(txt.strip())
# Ex 4.3
print(txt.upper())
#ex 4.4
print(txt.replace('U', 'V'))
#Ex 4.5
y = "I am proudly Ugandan"

for char in range(0, len(y)):
    if(char == 1 or char == 2 or char == 3):
        print(y[char])

#Ex 4.6
# x = "All "Data Scientists" are cool!"

m = "All \" Data Scientists \" are cool!"
print(m)


print("------------Dictionary-------------")
# Ex 5.1
Shoes  = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])
# Ex 5.2
Shoes['brand'] = "Adidas"
print(Shoes)
# Ex 5.3
Shoes.update({"type":"sneakers"})
print(Shoes)
# Ex 5.4
print(Shoes.keys())
# Ex 5.5
print(Shoes.values())
# Ex 5.6
if 'size'in Shoes:
    print('size'in Shoes, ":it does exist")
# Ex 5.7
for key, value in Shoes.items():
    print(key," , " ,value)
# Ex 5.8
Shoes.pop('color')
print(Shoes)
# Ex 5.9
Shoes.clear()
print(Shoes)

# Ex 5.10
car = {
    'type': 'BMW',
    'color': 'black',
    'speed': '200khr'
}


new_car = car.copy()
print(new_car)

# Ex 5.11
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