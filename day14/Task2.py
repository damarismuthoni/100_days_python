# You are about to purchase a ticket for something 
# or some chilling over the weekend. 
# You have to decide whether you will attend the movies or you’ll go for sport.
# Write a pseudocode that will take you through the steps of deciding what
# you will do and how much you will spend. Then convert that into a python code.

weather = 0

movie = "showing"
action = 0
romance = 1
comedy = 1

football = "matchDay"
arsenal = 1
psg = 1
manchester = 0

movie_ticket = 1300
football_ticket = 500

if(weather == 1):
    if(movie == "showing"):
        if(action == 1):
            print( "Lets Go watch an Action Movie")
    else:
        print("Conditions Not Suitable for a Movie")

elif weather == 0 :
    if( football == "matchDay"):
        if(psg == 1):
         print("Put on PSG Jersey. Let's Go watch Ball")
    else:
         print("Let's go Watch Ball")

else:
    print("Stay at home")

