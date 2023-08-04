# Advanced topics in Python

"""
 - Regular expressions
 - Generators and iterators
 - Decorators
 - Context managers 
 - Multithreading and multiprocessing 
"""

# Regular expressions
"""
    __Summary__
\d: Matches any digit (0-9)
\w: Matches any alphanumeric character (a-z, A-Z, 0-9,  and underscore)
\s: Matches any whitespace character (space, tab, newline)
.: Matches any character except a newline
*: Matches zero or more occurences of the preceding character or group
+: Matches one or more occurences of the preceding character or group
?: Matches zero or one occurence of the preceding character or group
[ ]: Matches any character within the square brackets
[^ ]: Matches any character not within the square brackets
^: Matches the start of the line 
$: Matches the end of a line 
"""
# matching and searching 
# regex re.match(), re.search(), re.findall()

# Example 1 Demonstrate regex | Match First Word, Match Group Word, Match all Numbers
# import re
# text = " Hello, my name is Martin Mugenyi. I am  a programmer with 10 years of experience"

# # Match First Word
# match = re.search(r"\b\w+\b", text)

# if match:
#     print('Matches: ',match.group())

# matches = re.findall(r"\d+", text)

# if match:
#     print('Matches: ',matches)

# Example 2 validate email format or email address
# import re

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

#     if re.match(pattern, email):
#         return True
#     else:
#         return False

# print(validate_email("maertinmugenyi26@gmail.com"))

# Generators and Iterators
# 'yield' generator
# Iterator '__iter__' "__next__" iterator

# def factorial(n):
#     # Return the factorial of a number
#     if n == 0:
#         yield 1
#     else:
#         #yield n * factorial(n-1)
#         fact = 1
#         for i in range(1, n+1):
#             fact *= i 
#         yield fact

# # Print the factorial of a number from 1 - 10
# for i in range(1, 10):
#     print(*factorial(i))

# Example 3
# def squares():
#     for i in range(1, 10):
#         yield i ** 2

# # Create an iterator object that yields the square of numbers from 1 - 10
# squares_iterator = squares()

# # Print the first 5 squares of numbers in range (1, 10)
# for i in range(1, 10):
#     print(next(squares_iterator))

# Decorators @my_decorator
# Decorators in Python allows you to modify the behavior of functions or classes without directly changing their source code

# def my_decorator(func):
#     def inner():
#         print("This is the decorator")
#         func()
#     return inner

# @my_decorator
# def outer_decorator():
#     print("This is outer decorator")

# outer_decorator()


# Context manager - is an object that defines a temporary context for a block of code
# Example 1: Demonstrate a context manager to open a file and returns a context manager instance

# def open_file(filename):
#     """Open a file and return a context manager instance"""
#     file = open(filename, "r")

#     def __enter__():
#         return file
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         file.close()
#         print('File has been closed')

#         return __enter__, __exit__
    
# with open_file("test.txt") as f:
#     contents = f.read()

# Example 2: Demonstrate a context manager using a time series
# import time

# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()

#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time = time.time()
#         execution_time = end_time - self.start_time
#         print(f'The time for this execution {execution_time} seconds elapsed')

# # with example usage
# with Timer():
#     """measure the execution time"""
#     time.sleep(2)

import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Usage example
with DatabaseConnection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users_1 ("+
   " id INT PRIMARY KEY,"+
    "username VARCHAR(255),"+
    "email VARCHAR(255),"+
    "password VARCHAR(255))"+";")
    results = cursor.fetchall()
    
    # Process the query results or perform other database operations
    for row in results:
        print(row)





# Day 7: Python for Data Science

"""
1. NumPy, Numerical Python, helps you work with arrays efficiently
2. Pandas - Functionalities, data cleaning, transformation, merging, filtering

Data Visualization
Plotting - use library called matplotlib or seabon - create - line, scatter, bar, histogram
heatmaps

Key concepts in Data Science:
1. Data - (text, images, videos) or semi structured data (JSON, XML)
2. Data Mining
3. Machine Learning
4. Statistical Analysis
5. Data Visualization
6. Big Data
7. Predictive Analysis
"""

"""
  __summary__
1. Problem definition
2. Data Acquisition data.gov, kaggle, databases, APIs, External datasets
3. Ensure data quality, data validation, cleaning and processing
# EDA Data Exploratory Analysis

# Data Preparation 
"""

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
# Usage example
with FileHandler("example.txt", "w") as file:
    file.write("Hello, world!")

# The file is automatically closed outside the `with` block
