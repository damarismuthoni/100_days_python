#Append mode we are adding new statements to the txt file
# we will be learning how the append function works

var_name = open("file1.txt",  "a")

var_name.write("I can't find my pen")
var_name.write("I really miss my desk")
var_name.write("I miss my previous house")
 
var_name.close()