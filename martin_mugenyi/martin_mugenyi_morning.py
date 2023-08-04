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

# Multithreading and Multiprocessing 
""" Techniques that can be used to improve performance of a Python program"""

# Multithreading is a technique where multiple threads are created within a single process.
# Multiprocessing is a technique where multiple threads are created.

# Example of multiprocessing
# import threading

# def task(name):
#     print(f'Running task {name}')

# # create multiple threads
# threads = []
# for i in range(10):
#     t = threading.Thread(target= task, args=(f'Thread {i}',))
#     threads.append(t)
#     t.start()

# # wait for all threads to finish 

# for t in threads:
#     t.join()

# Example 4: demonstrate use of multiprocessing

# import multiprocessing
# def process_task(name):
#     print(f'Processing task {name}')

# # create a pool of processes
# pool = multiprocessing.Pool(processes=5)

# # Submit multiple task to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))

# # Close the pool and wait for all processes to finish
# pool.close()
# pool.join()

# Exeercise 1
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
    file.write("My name is Mugenyi Martin")

# Exercise 3
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
    cursor.execute("CREATE TABLE users_2 ("+
   " id INT PRIMARY KEY,"+
    "username VARCHAR(250),"+
    "email VARCHAR(255),"+
    "password VARCHAR(255))"+";")
    


# Exercise 3
import threading
import multiprocessing
import time

def add_integers(n):
    result = 0
    start_time = time.time()
    
    while time.time() - start_time < n:
        result += 1
        print(f"Current result: {result}")
    
    print(f"Final Result: {result}")

def multithreading():
    durations = [1, 2, 3]  # Different durations in seconds
    
    # Create and start a thread for each duration
    threads = []
    for duration in durations:
        thread = threading.Thread(target=add_integers, args=(duration,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Run the threading method
multithreading()

# Exercise 4
 
# def add_integers(n):
#     result = 0
#     start_time = time.time()
    
#     while time.time() - start_time < n:
#         result += 1
#         print(f"Current result: {result}")
    
#     print(f"Final Result: {result}")

# def multiprocessing_example():
#     durations = [1, 2, 3]  # Different durations in seconds
    
#     # Create and start a process for each duration
#     processes = []
#     for duration in durations:
#         process = multiprocessing.Process(target=add_integers, args=(duration,))
#         process.start()
#         processes.append(process)
    
#     # Wait for all processes to finish
#     for process in processes:
#         process.close()
#         process.join()


# multiprocessing_example()
print('I tried to multiprocessing using my laptop and I failed.')

