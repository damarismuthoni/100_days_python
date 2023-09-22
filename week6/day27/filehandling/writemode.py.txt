# second part of the file handling lesson
# we will be writing using python on a txt file
# we will be showcasing methods of writing with python on a file

# write mode case study 1
var_name = open("file1.txt",  "w")

#write operation starts here

var_name.write("Hello World")
var_name.write("My name is Damaris")
var_name.write("This is the third statement")
var_name.write("Today is Monday")
var_name.write("I check my emails everyday")

var_name.close()

