# Tuples data structure 
# Tuples are ordered and non-changeable

phones = ("samsung", "iphone", "Techno")
print(phones)

phones = ("samsung", "iphone", "Techno", "samsung", "iphone", "Techno")
print(phones)

z = list(phones)
z.append("nokia")
phones = tuple(z)
print(phones)

#Add two tuples

laptops = ("Dell", "HP", "Acer")
laptop = ("samsung",)
laptops += laptop
Newstock = laptops + laptop
print(laptops)
print(laptop)
print(Newstock)

print("--------@@@@@-------\n")
# for loop in a tuple
for m in laptops:
    print(m)
print("--------@@@@@-------\n")
# Accessing tuple values
laptops = ("Dell", "HP", "Acer")
print(laptops[1])
print(laptops[2])
print(laptops[-3])

# length of a tuple
print(len(laptops))