# Calculate the Factorial of a number using a for loop.

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact = fact*i
print(fact)


# Calculate the Factorial of a number using a while loop.

num = int(input("Enter a number: "))
fact = 1
i = 1
while i<=num:
    fact = fact*i
    i+=1
print(fact)