# Exception Handling
"""
# Need for Exception Handling
  - The program terminates whenever an error occurs
  - Sudden termination can corrupt the program 
  - Exception may cause data loss 

# What is an exception?
 - An exception is a runtime error that terminates the execution of a program 

# What is Exception Handling?
 - Exception handling generates a message in correspondence to the occurence of an error and takes the right step to handle it.

# Types of errors
 - Compile time errors
 - Logical errors
 - Run-time errors

How an exception is handled?
  - Try block: tests the code if there's any exception to be handled
  - except block: Error message or piece of code output when there is an exception caught
  - else: No exceptions? run this code
  - finally: Always run this code
"""

print('----------------Exception Handling-----------------')
# Example to demonstrate Exception Handling
def divide(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    finally:
        print("Execution complete")

divide(10, 2)
divide(2,2)

# Example 
mental_health_degree = {
    1: "Severe: Requires immediate professional intervention. Individual is unable to function in daily life.",
    2: "Very high: Significant impairment in daily functioning. Professional help is essential.",
    3: "High: Noticeable impact on daily life. Professional assistance is strongly recommended.",
    4: "Moderately high: Some difficulty in fuctioning. Professional support is advisable.",
    5: "Moderate: Experiencing challenges but able to manage daily life with some effort.",
    6: "Moderately low: Mild impact on daily functioniong. Supportive measures may be beneficial.",
    7: "Low: Minimal impact on daily life. Minor support may be helpful",
    8: "Very low: Rarely interferes with daily functioning. Minimal support needed if any.",
    9: "Almost none: Negligible impact on daily life. No support required in most cases.",
    10: "None: No discernable impact on mental health. Individual is functioning optimally."
}

mental_health_rating = int(input("Please rate your mental_health on a scale of 1 - 10: \t"))


try:
    if(mental_health_rating < 1 or mental_health_rating > 10):
        print("Invalid input.")
except Exception as error:
    print("Error: ", error)
else:
         if mental_health_rating in mental_health_degree:
            print(mental_health_degree[mental_health_rating])
         else:
             print("Sorry, but we have nothing to say about your mental health")
finally:
    print("Execution complete.")

# Raising Exception we use the raise statement
# The raise statement allowas the programmer to force a specific exception to occur.
# The sole argument in raise indicates the exception to be raised. 
# This must be either an exception instance or an exception class (a class that derives from Exception).

# Example
# try:
#     raise NameError("Hi there")
# except NameError:
#     print("An exception has been caught")
#     raise





# File Handling in Python 
print('-----------File Handling---------')
"""
# What is file handling?
  - A file contains a collection of data and information
  - File handling performs functions such as creating, reading, updating and deleting files.

# Operations performed in file handling
  1. Open a file
  2. Read or write
  3. Close the file

Modes supported by the open()
  - 'r' -> Read - Default value. Opens a file for reading, error if the file doesn't exist
  - 'a' -> Append - Opens a file for appending creates the file if it doesn't exist
  - 'w' -> Write - Opens a file for writing, creates the file if it doesn't exist
  - 'x' -> Create- Creates the specified file, returns an error if the file exists
  - 't' -> Text- Default value. Text mode
  - 'b' -> Binary - Binary mode (e.g Images)
"""

# Example 1
file = open('test.txt', 'r')
for each in file:
    print(each)
print(file.read())

#  Example 2 using read()
with open('test.txt', 'r') as file:
    data = file.read()

print(data)

# Example 3 using the split() and readlines()
with open('test.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# Example 4 using write()
file = open('test.txt', 'w')
file.write('This is the write command')
file.write('It allows us to write in a particular file')
file.close()

# Example 5 
with open('test.txt', 'w') as f:
    f.write("Hello World!!!")

# Example 6
file = open('test.txt', 'a')
file.write('This will add this line')
file.write('My is Mugenyi Martin')
file.write('Software Engineering student')
file.close()

