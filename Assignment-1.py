# Question 1
print("Question 1\n")

# taking inout from user
number1 = int(input("Enter 1st no.: "))
number2 = int(input("Enter 2nd no.: "))
number3 = int(input("Enter 3rd no.: "))

# calculating average
average = (number1+number2+number3)/3
print(f"Average = {average}")

###############################################

#Question 2
print("Question 2\n")

#taking input of gross income and number of dependents
gross_income = float(input("Enter your Gross Income $"))
dependents = int(input("Enter no. of Dependents: "))

gross_income = round(gross_income, 2)

#subtracting standard deduction(10000) and dependent deduction(3000)
taxable_income = (gross_income-10000-dependents*3000)

#calculating tax( 20% of taxable income)
if taxable_income > 0:
    tax = taxable_income*0.20
else:
    tax = 0

print("Your tax = ",tax,sep="$")

###########################################

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

###########################################

#Question 4
print("Question 4\n")

# taking input from user
marks = []

for i in range(0, 5):
    marks_input = input("Enter marks of students: ")
    marks.append(marks_input)
    
#printing sorted marks
print(f"Sorted Marks: {sorted(marks)}")

###############################################

#Question 5
print("Question 5")
#making list of colors as specified
color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print("Part a")
#Part(a)-Removing 4th elemnt and printing new list
color.pop(3)

print(color)

print("Part b")
color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#part(b)- Removing "Black" and "Pink" from the list
color.remove('Black');color.remove('Pink'); color.insert(3,'Purple')
print(color)
