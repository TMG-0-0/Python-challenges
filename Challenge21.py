# WAP that guess the Number from 1-10 using for loop.

secret_num = 9

for i in range(11):
    guess = int(input("Enter any number from 1-10: "))
    if guess==secret_num:
        print("Congrats")
        break
    print("Wrong guess! Try again.")


# WAP that guess the Number from 1-10 using while loop.

secret_num = 7
guess = int(input("Guess the number between 1 to 10: "))

while guess != secret_num:
    print("Wrong guess! Try again.")
    guess = int(input("Guess again: "))

print("Congratulations! You guessed it right.")