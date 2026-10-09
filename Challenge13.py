# Create a tuple of your favorite fruits and display all the fruits.
# Access and print the first and last fruit in the tuple.
# Attempt to change the second fruit in the tuple and observe what happens (this should
# raise an error since tuples are unchangeable).
# Combine this tuple with another tuple of your favorite vegetables, and print the resulting combined tuple.
# Find and print the length of the combined tuple using the len() function.

fruits = ("Apple", "Orange", "Banana")
# fruits[1] = "Grape"
vegetables = ("Tomato", "Potato", "Onion")
Combine = fruits + vegetables
length = len(Combine)

print(f"All fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[2]}")
print(f"Combination: {Combine}")
print(f"Length: {length}")