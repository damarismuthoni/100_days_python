# Imagine you are about to prepare dinner,
# you have only a budget of sh. 1500,
# write a python code that will help you decide on what to buy to fit your budget 
# after deciding what you will have for dinner. 

budget = 1500
kfc = 1200
rice = 0
rice_price = 700
oil = 1
meat_price = 800
potato = 0


if (rice == 1):
    if (oil ==1):
        print("Let's Buy some meat and cook rice")
        change = budget - meat_price
        print("Our Change is", change)
    else:
        print("Buy some cooking oil")
        
elif (oil == 1 and rice == 0):
    if (potato == 1):
        print("Let's Cook some Fries")
    else:
        print("Buy Some potatos")

else:
    print("Let's Eat Some KFC")
