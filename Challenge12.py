# Create an empty list of type strings called days. Use the add method to add names of 7 days and
# print all days.

days = []
days.append("Sunday")
days.append("Monday")
days.append("Tuesday")
days.append("Wednesday")
days.append("Thursday")
days.append("Friday")
days.append("Saturday")
print(days)


# Add your 7 friend names to the list. Use where to find a name that starts with the alphabet a.

friends=["John", "Suraj", "Anmol", "Manish", "Ashok"]
a_names = [name for name in friends if name.lower().startswith("a")]
print("All friends:", friends)
print("Names starting with 'A':", a_names)