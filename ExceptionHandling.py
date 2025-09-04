'''
What is Exception Handling:
errors during execution are called exceptions

eg : print(10/0)
without handling it program crashes
'''

# try-except block

try:
    num = int (input("enter a number: "))
    print (10 /num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number entered")


# else and finally
# - > else: runs if no Exception occurs
# -> finally: always runs (clean up code)


# Raising Exceptions

def divide(a,b):
    if b == 0:
        raise ValueError("Denominatpr cannot be zero")
    return a / b

# print(divide(10,0))



#custom Exeption
# create your own excetion class (inherit from Exception)

class AgeToLowError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeToLowError("Age must be 18 or above ")
    print("valid age")

check_age(16)