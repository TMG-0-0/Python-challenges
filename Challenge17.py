# Create a function that finds a cube of a number.

def find_cube(num):
    return num ** 3
number = 5
print(f"The cube of {number} is {find_cube(number)}")


# Create a function that finds age from birth year.

from datetime import datetime

def find_age(birth_year):
    current_year = datetime.now().year
    return current_year - int(birth_year)

age = find_age(2007)
print(age)