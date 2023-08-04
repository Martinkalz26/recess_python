# Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating...")


# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...Woof!")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} is meowing...")

# # Create Animal Objects
# animal = Animal("Generic Animal")
# dog = Dog("Spot")
# cat = Cat("Fluffy")

# # Invoke call eat()
# animal.eat()
# dog.eat()
# cat.eat()

# dog.bark()
# cat.meow()



# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"Car brand: {self.brand}")
#         print(f"Car color: {self.color}")
        
#     def move(self):
#         print(f'{self.brand} is moving')

# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         super(Car, self).__init__(brand, color)
#         self.num_wheels = num_wheels

#     def display_info(self):
#         super(Car, self).display_info()
#         print(f"Number of wheels: {self.num_wheels}")

#     def honk(self):
#         print("Car is honking")


# my_car = Car("BMW", "Black", 4)

# # Access and modify the car attributes
# print("Brand:", my_car.brand)

# my_car.display_info()
# my_car.move()
# my_car.honk()

# Exercise 1 
# Demonstrate the using inheritance to calculate area and perimeter of circle and rectangle 
# respectively (Shape: circle)



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating...")

# class Flyable:
#     def fly(self):
#         print(f"{self.name} is flying...")

# class Bird(Animal, Flyable):
#     def __init__(self,name, species):
#         super().__init__(name)
#         self.species = species

#     def display_info(self):
#         print(f"Species: {self.species}")
#         print(f"Name: {self.name}")

# # create object
# my_bird = Bird("Pigeon", "bird")

# # Invoke the Bird methods
# my_bird.eat()
# my_bird.fly()
# my_bird.display_info()


# Method overriding 

# class Animal:
#     def make_sound(self):
#         print("Animal is making a sound!")

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog is barking!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Cat is meowing!")

# def make_animal_sound(animal):
#     animal.make_sound()

# # Create a objects
# animal = Animal()
# dog = Dog()
# cat = Cat()

# # Implement
# make_animal_sound(animal)
# make_animal_sound(dog)
# make_animal_sound(cat)


# Polymorphism allows you to write code that can work with different objects entails (method overloading and method overriding)

# Example 4
# class Shape:
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

# import math
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius**2

#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius

# # create shape objects
# rectangle = Rectangle(5, 5)
# circle = Circle(2)

# # Calculate and display Area
# print("Area of rectangle: ", rectangle.calculate_area())
# print("Area of circle: ", circle.calculate_area())

# Overloading functions
# class Calculator:
#     def add(self, x ,y):
#         return x + y

#     def add(self, x, y, c):
#         return x + y + z

# calc = Calculator()
# print(calc.add(5,5))
# print(calc.add(5,5,5))

# Abstration 
# Allow you to focus on essential features and hide them from unnecessary details

# Example 5:
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Starting the car...")

#     def stop(self):
#         print("Stopping the car")

# class Truck(Vehicle):
#     def start(self):
#         print("Starting the truck...")

#     def stop(self):
#         print("Stopping the truck")

# car = Car()
# truck = Truck()

# car.start()
# truck.start()
# car.stop()
# truck.stop()

# Exe 2 Demonstrate abstration using calculating area of a circle and rectangles

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

# create shape objects
rectangle = Rectangle(5, 5)
circle = Circle(2)

# Calculate and display Area
print("Area of rectangle: ", rectangle.calculate_area())
print("Area of circle: ", circle.calculate_area())



import tkinter as tk

def receipt():
    name = product_entry.get()
    price = float(price_entry.get())
    quantity_value = int(quantity.get())

    # Calculate the total for the product
    total = quantity_value * price

    # Add the product and its total to the receipt
    receipt_text.insert(tk.END, f"{name} \t {quantity_value} \t {price} \t {total}\n")

    # Update the overall total
    global overall_total
    overall_total += total
    total_label.config(text=f"Total: {overall_total}")

    # Clear the input fields
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity.set("1")

# Create the main window
window = tk.Tk()
window.title("Mugenyi And Sons Hardware")

# Create the receipt text widget
l = tk.Label(window, text='--------RECEIPT---------', font=("Times New Romans", 20, 'bold', 'italic'), fg='blue')
l.grid(row=0, column=1, padx=2, pady=5)

heading = tk.Label(window, text='Product\tQty\tPrice\tAmount',  font=("Times New Romans", 10, 'bold'))
heading.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

receipt_text = tk.Text(window, width=30, height=10, font=("Times New Romans", 10), fg="green")
receipt_text.grid(row=2, column=0, columnspan=10, padx=10, pady=10)

# Create the product entry field
product_label = tk.Label(window, text="Product:",  font=("Times New Romans", 20))
product_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
product_entry = tk.Entry(window)
product_entry.grid(row=3, column=1, padx=10, pady=5)

# Create the price entry field
price_label = tk.Label(window, text="Price:", font=("Times New Romans", 20))
price_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
price_entry = tk.Entry(window)
price_entry.grid(row=4, column=1, padx=10, pady=5)

# Create the quantity entry field
quantity_label = tk.Label(window, text="Quantity:", font=("Times New Romans", 20))
quantity_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
quantity = tk.StringVar(value="1")
quantity_entry = tk.Entry(window, textvariable=quantity)
quantity_entry.grid(row=5, column=1, padx=10, pady=5)

# Create the "Add Product" button
add_button = tk.Button(window, text="Add Product", font=("Times New Romans", 20), command=receipt)
add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create the total label
overall_total = 0.0
total_label = tk.Label(window, text="Total: 0.0", font=("Times New Romans", 20))
total_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Start the main GUI loop
window.mainloop()