# - Write a python program that will prompt the user to 
#input their credit card information and check whether the information shared is a string or an integercd

name = "Christie"
print("Hello " + name)
print(" Please Enter the Following information to continue...")

print("PIN")
pin = input()

print("Type of Transaction: Select One: ")
print(" * Deposit * ")
print(" * Withdrawal * ")
print(" * Transfer * ")
print(" * Balance * ")

transaction = input()

print(type(pin))
print(type(transaction))



