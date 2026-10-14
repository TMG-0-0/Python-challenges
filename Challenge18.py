# Write a program that prints sum of first n natural number using for loop.

n = int(input("Enter a number: "))
sum_n = 0

for i in range(1, n+1):
    sum_n+=i
    
print(f"The sum of the first {n} natural numbers is: {sum_n}")


# Write a program that prints sum of first n natural number using wile loop.

n = int(input("Enter a number: "))
sum_n = 0
i = 1

while i <= n:
    sum_n += i  #sum_n = sum_n + i
    i += 1

print(f"The sum of the first {n} natural numbers is: {sum_n}")