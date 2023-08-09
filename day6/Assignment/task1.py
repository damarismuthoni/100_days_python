# Attempt the following questions in code. You are expected to convert these logical operations to code in python. All the best
# Convert the following questions into lines of code:-

p = True
q = False
r = True

# (p∨¬q) and q
var_a = (p or not q)
ans_1 = (var_a and q)
print ( " Answer to Q1 = " + str(ans_1) )

# (p or q) not (¬q and ¬p)
var_b = (p or q)
var_c = (not (q) and not (p))
ans_2 = not(var_b != var_c)
print ( " Answer to Q2 = " + str(ans_2) )

# (p ∨ q) ∧ (p or  ¬ q)
var_d = (p or q)
var_e = (p or not q)
ans_3 = (var_d and var_e)
print ( " Answer to Q3 = " + str(ans_3) )

# p ∨ (q ∧ r) 
var_f = (q and r)
ans_4 = (p or var_f)
print ( " Answer to Q4 = " + str(ans_4) )

#¬(p ∧ q) ∨ (p ∨ q) 
var_g = not(p and q)
var_h = (p or q)
ans_5 = (var_g or var_h)
print ( " Answer to Q5 = " + str(ans_5) )






