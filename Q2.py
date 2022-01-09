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
