# - Write a python Program to prompt the user to create a shopping list and calculate the total cost

print("Karibu to Naivas")
print("What would you like Today?")

print("Mangoes? Enter Amount in kgs")
item1 = int(input())

print("Potatpes? Enter Amount in kgs")
item2 = int(input())

print("Rice? Enter Amount in kgs:" )
item3 = int(input())

print("Tomatoes? Enter Amount in kgs: ")
item4 = int(input())

total = (item1*27) + (item2*27) + (item3* 37) + (item1*30)

print("Your total is:  " + str(total) )