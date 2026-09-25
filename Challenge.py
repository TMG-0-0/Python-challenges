# Write down what you spend each day from Sunday to Saturday using a dictionary, add them up
# to find the total for the week, and figure out the average amount spent per day.

Week_spend = {
    "Sunday" : "200",
    "Monday" : "250",
    "Tuesday" : "150",
    "Wednesday" : "300",
    "Thursday" : "250",
    "Friday" : "300",
    "Saturday" : "350"
}
Ws=200+250+150+300+250+300+350
av= Ws/7

print(f"Total sum Week: {Ws}")
print(f"Average amt: {av}")