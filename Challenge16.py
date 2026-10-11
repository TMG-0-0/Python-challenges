# Write a program that takes a list of numbers and creates a new list containing the squares of all even numbers from the original list.

user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Squares of even numbers:", even_squares)


# Write a program that takes a dictionary of student names and their grades, and creates a new dictionary containing only the students who passed the exam (grade 50 or above).

# student_names = {'John': 90, 'Sheog': 60, 'Tim': 45, 'Alice': 75, 'Jack': 30}
# passed = {name: score for name, score in student_names.items() if score>=50}
# print(passed)

students = {}
num_students = int(input("How many students would you like to enter? "))

for _ in range(num_students):
    name = input("Enter student name: ")
    grade = float(input(f"Enter grade for {name}: "))
    students[name] = grade
passed_students = {name: grade for name, grade in students.items() if grade >= 50}

print(f"Students who passed: {passed_students}")