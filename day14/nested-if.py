# Case Study 1: Movie Ratings
    # Suppose you want to provide different recommendations
        # for movies based on their ratings. You'll have an outer condition based on the
 # rating range and an inner condition based on the specific rating.

rating = 4.5

if rating >= 1 and rating < 3:
    print("Not recommended")
else:
    if rating >= 3 and rating < 4:
        print("Fair recommendation")
    elif rating >= 4 and rating < 4.5:
        print("Good recommendation")
    elif rating >= 4.5 and rating <= 5:
        print("Highly recommended")
    else:
        print("Invalid rating")

# Case Study 2: Student Grading
#Let's consider a case where you want to assign grades to students based on their exam scores and attendance.

exam_score = 85
attendance_percentage = 90

if exam_score >= 90:
    if attendance_percentage >= 85:
        grade = "A"
    else:
        grade = "B"
elif exam_score >= 80:
    if attendance_percentage >= 85:
        grade = "B"
    else:
        grade = "C"
else:
    grade = "D"

print("Student grade:", grade)
