# they are used to store many items in a single variable

Afternoon = ["Trevor", "Martin", "Blessing"]
print(Afternoon[-3])
print(Afternoon[2])
print(Afternoon[0])

# list length
print(len(Afternoon))

Afternoon = ["Trevor", "Martin", "Blessing","Martin", "Blessing", "Mark", "Matilda"]

# Accessing lists elements by specifying a range of indexes
print(Afternoon[2:5])
print(Afternoon[1:])
print(Afternoon[:4])
print(Afternoon[2:])

# adding elements
Afternoon.append("Mary")
Afternoon.insert(2, "Polly")
print(Afternoon)

# remove list items
Afternoon.remove("Matilda")
Afternoon.pop(4)
print(Afternoon)

# list sorting
Afternoon.sort()
print(Afternoon)

# merging list
evening = ['Paul', 'Peter', 'Robert', 'Ritah']
day = Afternoon + evening
print(day)



