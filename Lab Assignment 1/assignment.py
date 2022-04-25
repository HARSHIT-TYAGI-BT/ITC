# Q1
print('Question-1')
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
print("The Average is:" , ((n1 + n2 + n3) / 3))

# Q2
print('Question-2')

# Input from user:
Income = float(input('Enter Gross Income in dollars to the nearest penny: '))
Dependents = float(input('Enter number of Dependents: '))

# Calculations
Taxable_Income = Income - 10000 - (Dependents * 3000)
Tax = Taxable_Income / 5

if (Taxable_Income <= 0):
    print('No Income tax')
else:
    print('Income tax =' , Tax)

# Q3
print('Question-3')
SID = int(input('Enter SID: '))
Name = str(input('Enter name: '))
Gender = str(input('Enter Gender(F, M, or U for Unknown): '))
Course_Name = str(input('Enter Course_Name: '))
CGPA = float(input('Enter CGPA: '))
Student = [SID,Name,Gender,Course_Name,CGPA]
print('Your data is:',Student)

# Q4
print('Question-4')

# Input from user
Marks_1 = float(input('Marks of A: '))
Marks_2 = float(input('Marks of B: '))
Marks_3 = float(input('Marks of C: '))
Marks_4 = float(input('Marks of D: '))
Marks_5 = float(input('Marks of E: '))

Marks = [Marks_1,Marks_2,Marks_3,Marks_4,Marks_5]
Marks.sort()
print('The sorted mark list is:',Marks)

# Q5a
print('Question-5a')
color1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color1.pop(3)
print(color1)

# Q5b
print('Question-5b')
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print(color2)
