#STRINGS
var_str = ' The lion is the king of the Savanna'
var_str2 = " Fish Live in Water"


#methods
# tO GET LENGTH OF STRING

length1 = len(var_str)
length2 = len(var_str2)

print (length1)
print (length2)

#you can also print without defining it in a variable
print (len(var_str))

#upper operation 

uppercase = var_str.upper()
print(uppercase)
 
 #printing lowercase
lowercase = var_str.lower()
print(lowercase)

#split method
split  = var_str.split()
print(split)

# REPLACE METHOD

a = "kenya"
b = a.replace("kenya", "  algeria")
print(b)
print(a)

#strip - to remove any white space before a string 

var_strip = b.strip()
print (var_strip)