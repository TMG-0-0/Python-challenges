# Print the first 10 terms of the Fibonacci sequence using a for loop.

terms = int(input("How many terms of the Fibonacci sequence would you like? "))

a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()


# Print the first 10 terms of the Fibonacci sequence using a while loop.

terms = int(input("How many terms of the Fibonacci sequence would you like? "))
a, b = 0,1
count = 0

print("Fibonacci sequence:")
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()