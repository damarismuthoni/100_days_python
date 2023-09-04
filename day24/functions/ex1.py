# Syntax  def()
# statements
# function call

# case study 1 .... printing function

def defineOutput():
    print('This is my first function ')

defineOutput()


#Case Study 2
# function to calculate the area of a triangle
base = 25
height = 16

def areaTriangle():
    area = base * height * 0.5
    print (area)
areaTriangle()

#case study 3 on functions
#Printing 3 statements within the function

statementA = "The Weather today is lovely"
statementB = " Coffee is sweater than tea"
statementC = "My favorite film is Thelma and Louise"
statementD = " The weekend was awesome"

#function3 starts here

def printStatement():
    a = statementA + statementB
    b = statementB + statementC
    c = statementA + statementD

    print(a)
    print(b)
    print(c)

printStatement()
