# You are about to interview a number of candidates for a job offer at the company you work at
#  or at your company. There are a number of repetitive operations that you need to do.

# Repetitive Operations:

# Check CV to eliminate or proceed
# Plan for interview
# Give feedback on interview

# CHECK CV TO ELIMINATE OR PROCEED
# INFINITE LOOPS

while True:
    candidate_qualification = input("Enter list of candidate qualifications: (comma separated) : ")
    qualification_list = candidate_qualification.split(',')
    experience_years = int(input("Experience Years: "))

    print (qualification_list)

    if 'laravel' in qualification_list and\
    'php' in qualification_list and\
    'javascript' in qualification_list and\
    'postgres' in qualification_list and\
    'sql' in qualification_list and\
     experience_years >=2 :
        
        print("The Candidate is Qqualified For the Position")
        print("Proceed to Next Phase")

        break

    else:
        print("The Candidate is Not Qualified")
        choice = input("Input Yes to Proceed No to Stop:")
        if choice.lower() == 'no' :
            break

    
