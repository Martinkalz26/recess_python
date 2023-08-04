# sets data structure
# unchangeable one can remove and add new items 

set_one = {"rice","matooke", "Irish"}
print(set_one)

# Duplicates in sets
set_one = {"rice","matooke", "Irish","Irish"}
print(set_one)

# Accessing set items 
for x in set_one:
    print(x)

# datatype of the set 
print(type(set_one))

# Length of the set
print(len(set_one))

# Add set items
set_one.add("posho")
print(set_one)

# Adding items from another set into the current set using update()
fruits_set = {'pineapple', 'mango', 'papaya'}
set_one.update(fruits_set)
print(set_one)

# Remove set item
set_one.remove('papaya')
print(set_one)

# Joining two sets using union()
sauce_set = {'beef', 'chicken', 'fish', 'groundnuts'}

set_two = set_one.union(sauce_set)
print(set_two)