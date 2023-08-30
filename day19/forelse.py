# FOR ELSE EXAMPLE - GOAL IS TO WAKE UP IN THE MORNING

work = 5
vacation = 3
day = 0

# for block() starts here

for i in range(work):
    day = day + 1
    if (day <=  work):
        print("Wake up Early !")
    else:
        print("You can sleep in")
    print("The day is", day)

else:
    day = day + 6
    if(day>work):
        print("You can wake up late")
    else:
        print("You can wake up early")
    print("The day is", day)