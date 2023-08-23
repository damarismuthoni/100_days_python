# This is a codelab for Nested Ifs
# We will do 3 examples to help you grasp the concepts
# Here is the syntax
# syntax
#if(criteria):
#    if(criteria b):
#        statement
#    elif(criteria c):
#        statements
#    else:
#        closing statement
        
#else:
#    if(criteria a):
#        statements
#    else:
#        statments

# Simple Nested if
#Case What to wear

weather = "sunny"
status = 0
color = "green"
occass = "official"
comfort = 0

# Nested if Structure
if(weather == "sunny"):
    if(color == "blue"):
        print("Wear the cloth")
    elif(status == 1):
        print("Wear the cloth!")
    else:
        print("Wear anything clean!")
else:
    if(color == "grey"):
        print(" Check the weather condition")
    elif(comfort == 1):
        print("You can wear it")
    
    else:
        print(" Look for something else to Wear")


# Second Nested If
# Tea or Coffe Decision

coffee = 1
tea = 1
sugar = 0
milk = 1
time = "morning"

# Nested If
if(time == "morning"):
    if(tea == 1):
        if(sugar == 1):
            if(milk == 1):
                print("You can have tea")
            else:
                print("You can have Black coffee!")
        else:
            print("Go buy Sugar")
    else:
        print(" You drink some hot water")
else:
    if(coffee == 1):
        if(sugar == 1):
            if(milk == 1):
                print(" You can have some mocha")
            else:
                print(" You can have some House Coffee")
        else:
            print(" You can have Nescafe 3 in 1")
    else:
        print("Include it in your next shopping list")


# Case 3 University selection
# Student Side decision
distance = 1        # 1 = near, 0 = far
clust = 34.5
convinience = 1     
upkeep = 0         # 1 = expensive , 0 = affordable
cost = 1            # 1 = affordable, 0 = expensive


# Nested If Structure
if (clust >= 35):
    if(convinience == 1):
        if(upkeep < 1):
            if(cost == 1):
                print(" Select the University")
            else:
                print("Look for another school")
        else:
            print("Look for an affordable school")
    else:
        print("Decide on whether to study only or work only")        
else:
    if(convinience == 1):
        if(upkeep == 0):
            print("You can do that course")
        else:
            print("Choose another course")
    else:
        print("Choose another university")
