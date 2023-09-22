
# Attempt the following questions in code
# a and  b ∧ ¬c =  a or (b ∧ (¬c)).
a = True
b = False
c= True
var_a = a and ( b and not c)
var_b = a or (b and not c)
ans_1 = var_a = var_b
print( "Answer to Q1 =  " + str(ans_1))

# (p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q).
p = True
q = False
var_c = (p and q)
var_d = (not p and q)
var_e = (not p and not q)
ans_2 = (var_c) or (var_d) or (var_e)
print("Answer to Q2 = " + str(ans_2))
