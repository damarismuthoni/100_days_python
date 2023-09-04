for number in range(0, 6):
    print('Person',  number)

successfull = True
for number in range(3):
    print("Attempt")
    if successfull:
        print("Successfull")
        break
else:
    print("Attempted 3 times and Failed")