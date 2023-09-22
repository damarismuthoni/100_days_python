# implementation of a try, except, else exception handling in python
#lets create a simple logic for taking stairs or wait for an elevator
ascending = True
descending = False
luggage = "significant"
tired = True

try: 
  if(ascending == True and luggage == "significant"):
    print("Wait for Elevator")
  try:
    if(ascending == True or descending == True or tired == True):
      print("Stairs sound OK")
  finally:
    print("Some exercise for me")
except:
  print("No stairs today")
else:
  if(descending == True and luggage == "minimal"):
    print("Let's take the stairs")
  