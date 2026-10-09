# Create a set of your favorite hobbies. Add a few more hobbies to the set, then remove one.
# Finally, perform a union with another set of hobbies and find the common ones using intersection.

hobbies = {" Play Football", "Dance", "Sing", "Read Books"}
hobbies.add("Build AI Agents")
hobbies.remove("Dance")
hobbies2 = {"Sing", "Travel", "Read Books"}
union = hobbies .union (hobbies2)
intersection = hobbies .intersection (hobbies2)
print(f"Union: {union}")        # print("Union:", union)
print(f"Intersection:{intersection}")
print(hobbies)