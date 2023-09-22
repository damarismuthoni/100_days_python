# - Write a python program that will prompt the user to perform 
#the calculations of Area, surface area and volume of a cuboid
print("Cuboid calculations")
print ("Input Length")

len = int(input())

#AREA
area = len*len*len
print("The area of the cuboid is: " + str(area))  

#SURFACE AREA
surfaceArea = 2*(len*len) + 2*(len*len) + 2*(len*len)
print("The Surface Area of the cuboid is : " + str(surfaceArea))

