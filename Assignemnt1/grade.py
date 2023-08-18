# Input class score
class_score = int(input("Enter the class score: "))

# Determine the letter grade based on the score
if class_score >= 90:
    grade = 'A'
elif class_score >= 80:
    grade = 'B'
elif class_score >= 70:
    grade = 'C'
elif class_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the letter grade
print("Letter Grade:", grade)
