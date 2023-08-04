
# class Bank:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

    # def deposit(self, amount):
    #     self.balance += amount

    # def withdraw(self, amount):
    #     if self.balance >= amount:
    #         self.balance -= amount
    #     else:
    #         print('Insufficient balance')

    # def display(self):
    #     print("Account number: ", self.account_number)
    #     print("Balance: ", self.balance)

# my_account = Bank(1111100000, 200000)
# my_account.deposit(100000)
# my_account.display()
# my_account.withdraw(150000)
# my_account.display()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return print('Area of a rectangle: ',self.length * self.width)

    def perimeter(self):
        return print('Perimeter of a rectangle: ',self.length + self.width)

rectangle_1 = Rectangle(10, 4)
rectangle_1.area()
rectangle_1.perimeter()

class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print('Name: ', self.name)
        print('Year: ', self.year)
        print('Course: ', self.course)

student_1 = Student('Mugenyi Martin', 3, "BSSE")
student_1.display_details()

class Circle:
    def __init__(self, radius):
        self.radius =radius

    def area(self):
        return print('Area: ',3.14 * self.radius * self.radius)

    def circumference(self):
        return print('Circumference: ',2 * 3.14 * self.radius)

circle_1 = Circle(3)
circle_1.area()
circle_1.circumference()

# Ex 2
# Calculate and display employee bonuses(15%) of salary (employee_1, 150000, employee_2, 230000)

class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def calculate_bonus(self):
        return print('Employee bonus: ', self.salary * 0.15, 'for ', self.name)

emp_1 = Employee('Martin', 150000)
emp_1.calculate_bonus()
emp_2 = Employee('Peter', 230000)
emp_2.calculate_bonus()

# Encapsulation
'''
1. To hide the implementation details of an object
2. To protect the object from changes
3. To protect the object from external changes 
4. Code organization and modularity
'''

class Bank_Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number # Encapsulate the account number attribute
        self._balance = balance # Encapsulates the balance attribute

    def deposit(self, amount):
        self._balance += amount # Encapsulate the deposit method

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount # Encapsulates the withdraw method
        else:
            print('Insufficient balance')

    def get_balance(self):
        return self._balance

my_account = Bank_Account("11112222", 1000)

print(my_account._account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account._balance)
my_account.withdraw(200)
print(my_account._balance)


class Temperature:
    def __init__(self, temperature):
        self.__temperature = temperature

    def convert_temperature_to_fahrenheit(self):
        return (self.__temperature * 9/5) + 32

temp = Temperature(37)
temp.__temperature = 100 # the temperature doesn't change 
print(f"{temp.convert_temperature_to_fahrenheit()} F")



# Assignment 2
# Show encapsulation with employee information to give a pay increment to (Salary with employee information to new_salary) e.g from 850000 to 1000000
class Employee:
    def __init__(self, name, employee_id , salary):
        self._name = name
        self._employee_id = employee_id
        self._salary = salary

    def pay_increment(self, salary):
        self._salary = salary
        return self._salary

    def display_employee_info(self):
        print('Name: ', self._name)
        print('Employee ID: ',self._employee_id)
        print('Salary: ', self._salary)

employee = Employee('Jack Reacher',"P001", 850000)
print('Employee information before pay increment')
employee.display_employee_info()
employee.pay_increment(1000000)
print('Employee information after pay increment')
employee.display_employee_info()


