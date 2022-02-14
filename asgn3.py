#Question 1

print("Question 1")
#taking input
sentence = input("Please give an input- ")
sentence=sentence.lower().strip()
i=0
#declaring empty dictionary for later to store element, eliminating common letters and words and counter pairs 
dict={}

#checking if the string input is a word or a sentence
if " " not in sentence:
     #searching for common elements
     while i<len(sentence):
          counter=0
          k=0
          while k<len(sentence):
               if sentence[i]==sentence[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          #storing values in dictionary
          dict[f"{sentence[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(sentence)
     #searching for the common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

#################################################################################

#Question 2
print("Question 2")
#Function for checking if  given year is a leap year or not
def is_leap_year(year: int) -> bool:                                                                                
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    #Condition for given constraints in question
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
     #Condition for 31 days in a 30 day month
    if month in (4,6,9,11) and date == 31:                                                                          
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
     #Condition for no. of days in February
    elif month == 2 and date >= 29:                                                                                 
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
          #Setting no. of days in the given month
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
    #incrementing the date
if date == max_days:                                                                                                
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))
 

######################################################################################
# Question 3

print('Qustion 3')

list = [3, 7, 9, 10]
list_out = []
for num in list:
    list_out.append((num, num**2))
print(list_out)

######################################################################################
#Question 4

print("Question 4")
grade=int(input('Enter Grade Points- '))

dict={10:{'grade_inp':'A+','remarks':'Outstanding'},
           9:{'grade_inp':'A','remarks':'Excellent'},
           8:{'grade_inp':'B+','remarks':'Very Good'},
           7:{'grade_inp':'B','remarks':'Good'},
           6:{'grade_inp':'C+','remarks':'Average'},
           5:{'grade_inp':'C','remarks':'Below Average'},
           4:{'grade_inp':'D','remarks':'Poor'}}
if 3<grade<11:
    for key in dict.keys():
        if key==grade:
            value=dict[key]
            print(f"Your Grade is {value['grade_inp']} and {value['remarks']} performance ")
        else:
            continue
else:
    print('Error!')

###############################################################################################################
#Question 5
    
print('Question 5')

string = "ABCDEFGHIJK"
i = 0
while len(string) - i*2 >= 1:
    print(" "*i + string[0 : len(string) - i*2])
    i = i + 1
    
 
#########################################################################################################################
#Question 6

print("Question 6")
condition=True

#creating dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Please Enter SID of Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part d")
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")

##############################################################################################################
#Question 7

print("Question 7")
number=int(input("Total elements of Fibonacci sequence that you want(it must be greater than 1)- "))

#using the formula of the sum of previous two terms is equal to the present term.
a1=1
a2=0
n=0
#initializing sum with first two terms
sum=a1+a2

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {number} terms")
print(a2)
print(a1)

#Printing the remaining fibonnaci terms
while n<number-2:
    a3=a2+a1
    a2=a1
    a1=a3
    print(a3)
    n=n+1
    sum+=a3
average=sum/number
#printing the program end prompt
print(f"Average of total {number} terms of sequence is {average}")
print("END")

##################################################################################################################
#Question 8

print('Question 8')

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
print("a", set1 ^ set2, '\n')

print("b", set1 ^ set2 ^ set3, '\n')

print("c", (set1 | set2 | set3) - (set1 ^ set2 ^ set3) - (set1 & set2 & set3), '\n')

set4 = set()
for n in range(1, 11):
    if n not in set1:
        set4.add(n)
print("(d)", set4, '\n')

print("(e)", set(range(1, 11)) - (set1 | set2 | set3), '\n')


