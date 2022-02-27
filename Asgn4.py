print("Question 1")
print("Solution 1 :-")
print("")
def TowerOfhanoi(n, fro, to, aux):
    if n == 0:
        return
    
    TowerOfhanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    TowerOfhanoi(n-1, aux, to, fro)

#calling TOH funtion 
TowerOfhanoi(3, 'A', 'C', 'B')
print("")

######################################################################################################

print("Question 2")
print(" ")
print(" ")
#take input of rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursion
print("\nusing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)


print("\nUsing loops:\n")
for line in range(1, n+1):

    
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

########################################################################################################

print("Question #3")
print(" ")
#Question3

n1=int(input("\nEnter an Integer:"))
n2=int(input("Enter another Integer:"))
#Making a list of return values
list1=list(divmod(n1,n2))
#a1=Quotient
q=list1[0]
#a2=Remainder
r=list1[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")

#Que3.a
print("\nQue3.a")
c1=callable(divmod(n1,n2))
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")
#Que3.b
print("\nQue3.b")
#list of values
listv=[q,r]
zero=False
if zero in listv:
    zero=True
else:
    zero=False
if zero==True:
    print("All result values are NOT 'non-zero'")
elif zero==False:
    print("All result values are 'non-zero'")
#Que3.c
print("\nQue3.c")
#new values of list
listr=[q,r]
for i in range (4,7):
    listr.append(i)
print(f"Appended (4,5,6) in the values ({q},{r})")
listv2=[]
#adding number > 4 from listr to listv2
for i in listr:
    if i>4:
        listv2.append(i)
#a new list listv3 with same elements as listv2 but in string form
listv3=list(map(str,listv2))
#Using join
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
#Que3.d
print("\nQue3.d")
set1={1,2}
set1.clear()
#adding above result in set datatype
for el in listv2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)
#Que3.e
print("\nQue3.e")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")
#Que3.f
print("\nQue3.f")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")

#######################################################################################################
print("Question #4")
print(" ")
print(" ")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating the object
student1 = Student("Nimar Kalra",21105075)
print("Object created")

#printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#deleting the object at the end
del student1
print("")

######################################################################################################

print("Question 5")
print(" ")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#updating salary
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#deleting a record
print("b. ", end='')
del employee3

print(" ")

#######################################################################################################

print("Question 6")
print(" ")
print(" ")
#taking input of a word from the first friend
word = input("Enter the first word: ")

#taking input of a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")

#dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#testing
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print("")
########################################################################################################
