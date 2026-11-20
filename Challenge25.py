# Ask the user for an integer and determine whether it is prime using a for loop.

num = int(input("Enter an integer: "))

if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# Ask the user for an integer and determine whether it is prime using a while loop.

num = int(input("Enter an integer: "))
i = 2
if num <= 1:
    is_prime = False
else:
    is_prime = True
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i+=1

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")