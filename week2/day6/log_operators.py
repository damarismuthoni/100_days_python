p = True
q = False
r = True

var_1 = (p or q)
ans_1 = (var_1 and r )

# print(ans_1)

var_2 =( p and r )
var_3 =(q and r) 

ans_2 = (var_2 or var_3)
ans_3 = (ans_1 or ans_2 )

print ( ans_3)