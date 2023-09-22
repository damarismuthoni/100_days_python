# input variables 
salary = int(input("Enter Your Income: "))
sidehustle = int(input("Enter Your Income from sidehustle"))

#Expense

utilityBills = int(input("Enter Your Utility Expenses"))
grocery = int(input("Enter Your Grocery Espense"))
allowances = int(input("Enter Your Allowances"))

# Goals
goal1 = "improve my setup"
goal2 = "Travelling"
goal3 = "Start a business"
goal4 = "Educating my Children"

mygoal = goal1
#Using elif for logic

if (mygoal == goal1):
    newincome = salary + sidehustle
    if(newincome >= 40000):

        totalexpense = utilityBills + grocery + allowances
        savings = newincome - totalexpense
        new