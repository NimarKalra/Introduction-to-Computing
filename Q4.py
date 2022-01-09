#Question 4
print("Question 4\n")

# taking input from user
marks = []

for i in range(0, 5):
    marks_input = input("Enter marks of students: ")
    marks.append(marks_input)
    
#printing sorted marks
print(f"Sorted Marks: {sorted(marks)}")