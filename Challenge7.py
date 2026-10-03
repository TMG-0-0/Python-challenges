# Write a number guess game which generate number from 1 to 6

import random
guess=int(input("Enter random number 1-6: "))

secret_num=random.randint(1,6)
print("Randomnum", secret_num)
if(guess==secret_num):
    print("Guess is correct!")
else:
    print("Not correct")