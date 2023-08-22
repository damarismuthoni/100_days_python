# Career scenario. Write a code that will help you 
# decide on what will influence your career choice. -->

choice_1 = "Dentist"
choice_2 = "Phamacist"
choice_3 = "pediatrician "
choice_4 = "Surgeon"

skill_1 = "Manual dexterity"
skill_2 = "Attention to detail"
skill_3 = "Compassion and patience"
skill_4 = "Problem-solving skills:"

list1 = [skill_1, skill_2, skill_3, skill_4]

print(" What skill set do you have")
print(list1)

my_skill = input("")
print("Your Skill is " + my_skill)

if(my_skill == skill_1):
    print(" You are best suited to ba a " + choice_1)

elif(my_skill == skill_2):
    print(" You are best suited to ba a " + choice_2)

elif(my_skill == skill_3):
    print(" You are best suited to ba a " + choice_3)

else:
    print("Your are best suited to be a " + choice_4)
    