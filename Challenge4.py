# Write a program that takes the ages of two people as input from the user. Compare their
# ages using comparison operators (==, !=, >, <, >=, <=) and print messages indicating the
# results (e.g., "Person 1 is older than Person 2").

A=int(input("Enter Person A Age: "))
B=int(input("Enter Person B Age: "))

if(A>B):
    print("Person A is older than Person B")
elif(A==B):
    print("Person A and Person B are same Age")
else:
    print("Person B is older than Person A")


# Write a program that takes the age and citizenship status of a person as input from the
# user. Use logical operators (and, or, not) to determine if the person is eligible to vote
# (age >= 18 and is a citizen). Print an appropriate message based on the result.

age=int(input("Enter Age: "))
is_citizen_input=input("Are you a Citizen? (yes/no): ").lower()

is_citizen=is_citizen_input=="yes"

if age>=18 and is_citizen:
    print("Eligible to vote")
else:
    print("Not Eligible")


# Write a program that initializes a list of books available in a library. Take the name of a
# book as input from the user and check if it is available in the library using membership
# operators (in, not in). Print a message indicating whether the book is available or not.

library_books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Sick", "Pride and Prejudice"]
requested_book = input("Enter the name of the book you are looking for: ")
if requested_book in library_books:
    print(f"Yes, {requested_book} is available in the library!")
else:
    print(f"Sorry, {requested_book} is not available in the library.")