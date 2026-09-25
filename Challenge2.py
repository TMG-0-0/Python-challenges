# Write a program that takes user input for year of birth (as a string) in the format 'YYYY’ and find
# the age of the person.

birth_year = int(input("Enter your birth year (YYYY): "))
current_year = 2026

age = current_year - birth_year

print(f"You are {age} years old.")
print(type(birth_year))