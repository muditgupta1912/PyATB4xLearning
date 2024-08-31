# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# Step 1 -> User Inputs -> score or marks -> int
# Step 2 ->  O/p -> str -> A or B....

# programme

Score = int(input("Enter your score"))
if 90 <= Score <= 100:
    print("Grade is A")
elif 80 <= Score <= 89:
    print("Grade is B")
elif 70 <= Score <= 79:
    print("Grade is C")
elif 60 <= Score <= 69:
    print("Grade is D")
else:
    print("Grade is F")
