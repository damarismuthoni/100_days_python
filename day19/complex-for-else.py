my_list = [1, 23, 38, 28, 49, 19, 3, 48, 33, 69, 60]
patt = "x"

#for(bock starts)
for i in my_list:
    if (i<69):
        patt = patt*9
        print(patt)
    elif(i<60):
        patt = patt*8
        print(patt)
    elif(i<49):
        patt = patt*7
        print(patt)
    elif(i<48):
        patt = patt*6
        print(patt)
    elif(i<38):
        patt = patt*5
        print(patt)
    elif(i<33):
        patt = patt*4
        print(patt)
    elif(i<28):
        patt = patt*3
        print(patt)
    elif(i<23):
        patt = patt*2
        print(patt)
    elif(i<19):
        patt = patt*1
        print(patt)
    else:
        patt = patt*0
        print(patt)
    break
else:
    if (i<=69):
        print(my_list)
    else:
        print(patt)

    
    