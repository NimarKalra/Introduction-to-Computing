#Question 3
print("Question 3\n")

# taking input from the user
SID = int(input("SID: "))
name = input("Name: ")
gender = input("Gender(F/M/U): ")
course_name = input("Course Name: ")
CGPA = float(input("CGPA: "))

# collecting and printing data in a list
student = [SID, name.title(), gender.upper(), course_name.title(), CGPA]
print(f"Student: {student}")
