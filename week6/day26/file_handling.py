# we are going to write operations to do
# all three operations read, write and append

var_name = open("statements.txt", "w")
var_name.write("The teacher wants us to do this on our own\n")
var_name.write("This is the next statement\n")
var_name.write("Today's lesson was great\n")
var_name.write("It didn't rain today\n")

var_name.close()

file_read=open("statements.txt", "r")

print(file_read.read())

var_name = open("statements.txt", "a")
var_name.write('I have received a reverse call request\n')
var_name.write("the girl is focused...nothing can distract the girl\n")
var_name.write("I am proud of myself \n")

var_name.close()

file_add = open("statements.txt", "r")

for i in var_name: 
    print(i)

