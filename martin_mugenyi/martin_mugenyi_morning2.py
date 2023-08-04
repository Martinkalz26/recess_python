# Basic Operators and Expressions (Input and Output operators)
"""
Arithmetic Operators
+ Addition
-Subtraction
* Multiplication
/ Division
// Divide return the quotient without the remainder
% Modulus
** Exponential

Comparison Operators
== Equal to
!= Not Equal !==
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

Logical Operators
Logical AND 'and'
Logical OR 'or'
Logical NOT 'not'

Assignment Operators
Assign value: '='
Add and assign value: '+='
Subtract and assign value: '-='
Multiply and assign value: '*='
Divide and assign value: '/='
Modulus and assign value: '%='
Exponentiate and assign value: '**='

Membership Operators
In: 'in' operator: checks if a value exists in a sequence
Not in: 'not in' operator: checks if a value does not exist in a sequence

Identity Operators:
Is: 'is' operator: checks if two values are the same
Is not: 'is not' operator: checks if two values are not the same 
"""

# # Examples of arithmetic operators
# # Addition
# a = 50 + 45
# print(a)
# # Subtraction
# b = 50 - 45
# print(b)
# # Multiplication
# c = 50 * 45
# print(c)
# # Division
# d = 50 / 45
# print(d)
# # Dividing without a remainder
# e = 50 // 42
# print(e)
# # Modulus
# f = 10 % 4
# print(f)
# # Exponential
# g = 2 ** 4
# print(g)

# # Examples of comparison operators
# h = 15
# i = 9
# # Greater than
# if h > i:
#     print('h is greater than i')
#     print(h > i)

# # Less than
# if h < i:
#     print('h is less than i')
#     print(h < i)

# # Greater than or equal to
# if h >= i:
#     print('h is greater than or equal to i')
#     print(h >= i)

# # Less than or equal to 
# if i <= h:
#     print('h is less than or equal to i')
#     print(i <= h)

# # Equal to
# if 10 == 10:
#     print('10 is equal to 10')
#     print(10 == 10)

# # Not equal to
# if h != i:
#     print('h is  not equal to i')
#     print(h != i)


# # Examples of logical operators
# a  = True
# b = False

# # Logical AND
# print(a and b)

# # Logical OR
# print(a or b)

# # Logical NOT
# print(not b)
# print(not a)

# # Assignment operators
# a = 5

# # Add and assign 
# a+=5
# print(a)

# # Add and assign 
# b = 20
# b -=5
# print(b)

# # Multipy and Assign
# c = 6
# c *= 5
# print(c)

# # Divide and Assign
# d = 7
# d /= 5
# print(d)

# #Modulus and Assign
# e = 8
# e %= 5
# print(e)

# #Exponential and Assign
# f = 9
# f **= 5
# print(f)

# # Membership Operators
# cars = ['Jeep', 'Tesla', 'BMW']

# if "BMW" in cars:
#     print('BMW' in cars)
#     print('toyota' in cars)

# # Identity operator
# z = [1,2,3,4,5,6,7]
# w = [1,2,3,4,5,6,7]
# print(z is w)
# print(z is not w)

# s =10
# k = 10

# print(s is k)

#Bitwise
"""
Bitwise operators are used to perfom operations on individual bits of binary numbers

Bitwise AND ('&'): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR ('|'): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR ('^'): Performs a bitwise XOR operation
Bitwise NOT ('-'): Performs a bitwise NOT operation between the corresponding bits of two integers
Bitwise left shift ('<<'): Performs a bitwise left shift operation 
Bitwise right shift ('>>'): Performs a bitwise right shift operation 
"""

# # Example of Bitwise operations
# a = 10
# b = 20
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(a - b)
# print(a << b)
# print(a >> b)


# Example of a calculator
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def main():
#     print('Jeff Simple Calculator')
#     number1 = float(input("Enter the frist number: "))
#     number2 = float(input("Enter the second number: "))
#     operator = input("Enter the operator(+, -, *, /): ")

#     if operator == '+':
#         result = add(number1, number2)
#     elif operator == '-':
#         result = subtract(number1, number2)
#     elif operator == '*':
#         result = multiply(number1, number2)
#     elif operator == '/':
#         result = divide(number1, number2)
#     else:
#         print('Invalid operator')
#     print('Result: ', result)


# if __name__ == '__main__':
#         main()


from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Martin Mugenyi Simple Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff',font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11,height=4, text='(', relief='flat',bg='white', command=lambda:self.show('(')).place(x=0,y=50)
        Button(width=11,height=4, text=')', relief='flat',bg='white', command=lambda:self.show(')')).place(x=90,y=50)
        Button(width=11,height=4, text='%', relief='flat',bg='white', command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=11,height=4, text='1', relief='flat',bg='white', command=lambda:self.show(1)).place(x=0,y=125)
        Button(width=11,height=4, text='2', relief='flat',bg='white', command=lambda:self.show(2)).place(x=90,y=125)
        Button(width=11,height=4, text='3', relief='flat',bg='white', command=lambda:self.show(3)).place(x=180,y=125)
        Button(width=11,height=4, text='4', relief='flat',bg='white', command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=11,height=4, text='5', relief='flat',bg='white', command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=11,height=4, text='6', relief='flat',bg='white', command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=11,height=4, text='7', relief='flat',bg='white', command=lambda:self.show(7)).place(x=0,y=275)
        Button(width=11,height=4, text='8', relief='flat',bg='white', command=lambda:self.show(8)).place(x=180,y=275)
        Button(width=11,height=4, text='9', relief='flat',bg='white', command=lambda:self.show(9)).place(x=90,y=275)
        Button(width=11,height=4, text='0', relief='flat',bg='white', command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=11,height=4, text='.', relief='flat',bg='white', command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=11,height=4, text='+', relief='flat',bg='white', command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=11,height=4, text='-', relief='flat',bg='white', command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=11,height=4, text='/', relief='flat',bg='white', command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=11,height=4, text='*', relief='flat',bg='white', command=lambda:self.show('*')).place(x=270,y=125)
        Button(width=11,height=4, text='=', relief='flat',bg='lightblue', command=self.solve).place(x=270,y=350)
        Button(width=11,height=4, text='c', relief='flat',bg='red', command=self.clear).place(x=0,y=350)

    def show(self,value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()