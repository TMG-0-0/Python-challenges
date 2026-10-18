# John wants to print his name 5 times, but each time with a number in front of it. WAP using for & while loop.

i = 1
for i in range(i,6):
    print(f"{i}.john")

i=1
while i<=5:
    print(f"{i}. john")
    i+=1


# WAP to print the multiplication tables of any number using for & while loop.

n = int(input("Enter a number: "))
for i in range(1,11):
    z = n*i 
    print(f"{n} x {i} = {z}")

n = int(input("Enter any number: "))
i = 1
while i<=10:
    z = n*i
    print(f"{n} x {i} = {z}")
    i=i+1