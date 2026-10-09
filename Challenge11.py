# Write a program that calculates the total and average of the following list of numbers, stopping if
# a negative value is encountered (using break), and skipping any zero values (using continue).

values = [10, 0, 25, 0, 50, -1, 40]

total = 0
count = 0

for value in values:
    if value < 0:
        print("Negative Value Encountered!")
        break
    if value == 0:
        continue
    
    total += value
    count += 1

avg = total / count if count > 0 else 0

print(f"Total: {total}")
print(f"Average: {avg}")