# Write a program that uses assert to check if a person's age is positive.

num=int(input("Enter Person's Age: "))
age=num
assert age>0, "Age cannot be Negative!"
print("Positive!")