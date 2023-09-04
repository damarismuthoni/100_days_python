week = 7
toothpaste=1
toothbrush=1
bakingsoda=5
mirror=1
water=7

#nestedfor
for i in range(0,week):       
    for j in range(water):
        for w in range(bakingsoda):
            if(toothpaste==1):
                if(toothbrush==1):
                    print("You can brush your teeth!")
                else:
                    print("Go buy a new Toothbrush")
            else:
                print("Go buy toothpaste")
        else:
            if(toothpaste==1 and toothbrush==1):
                print("Go and brush your teeth")
                breakC