import time  #module for time  

# A simple decorator to check how long a function takes to run
def timer_decorator(my_function):
    def wrapper():
        start = time.time()  # start 
        my_function()  # function call
        end = time.time()  # stop 
        print("Time taken:", end - start, "seconds")
    return wrapper  # return the new function

# Use the decorator
@timer_decorator
def say_hello():
    time.sleep(1)
    print("Hello!")

# function call
say_hello()