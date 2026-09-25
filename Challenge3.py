# Write a program that checks if a given number is even or odd. Take user input for the number,
# perform the check, and print the result.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")