# Write a Python program that takes a user's full name as input and Convert the full name to title
# case (capitalize the first letter of each word). Also remove trailing and leading space.

user_name=input("Enter full name: ")
upper=user_name.upper()
lower=user_name.lower()
title=user_name.title()
capitalize=user_name.capitalize()
strip=user_name.strip()
replace=user_name.replace("beautiful", "handsome")

print(f"Upper Case: {upper}")
print(f"Lower Case: {lower}")
print(f"Title Case: {title}")
print(f"Capitalize Case: {capitalize}")
print(f"Strip Case: {strip}")
print(f"Replace Case: {replace}")