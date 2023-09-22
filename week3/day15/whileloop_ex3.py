pressure = 15
max_opens = 3

# while loop
while (pressure < 35 and max_opens <8):
    pressure = pressure + 5
    max_opens = max_opens + 1
    print("The pressure is", pressure)
    print(" The Tap is opened only ", max_opens)