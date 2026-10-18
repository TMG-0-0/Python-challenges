# Count how many digits are in a positive integer without converting it into a string using for loop.

number = int(input("Enter a positive integer: "))

if number == 0:
    count = 1
else:
    count = 0
    num = number
    for _ in range(100):
        if num > 0:
            count += 1
            num //= 10
        else:
            break

print(f"Number of digits: {count}")


# Count how many digits are in a positive integer without converting it into a string using while loop.

number = int(input("Enter a positive integer: "))
count = 0
num = number

while num > 0:
    num = num // 10
    count += 1

print(f"Number of digits: {count}")