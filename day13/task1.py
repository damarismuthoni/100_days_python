# Shopping scenario.
#  Write a code that will help you to decide the budget of the things you want to go shopping for
#  and determine how many items you get to buy with that budget.

shop_status1 = "open"
shop_status2 = "closed"

item1 = "groceries"
item2 = "stationaries"
item3 = "clothes"
item4 = "detergents"


budget_item1 = 8000
budget_item2 = 1800
budget_item3 = 5000
budget_item4 = 4800

assigned_budget = 4000

# if(shop_status1):
#     print("shop open proceed to shop")

# if assigned_budget == 10000:

#     print("Assigned budget is 10000! Let's Spend")

if assigned_budget >= budget_item1:
    print("Add " + item1 + " To Cart")

elif assigned_budget >= budget_item2:
    print("Add " + item2 +" To Cart")

elif assigned_budget >= budget_item3:
    print("Add" + item3 + "To Cart")

elif assigned_budget >= budget_item4:
    print("Add" + item4 + "To Cart")

else:
    print("Budget Not Sustainable")
