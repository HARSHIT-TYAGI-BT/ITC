Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#question 5

# Ask for No. of Atoms
No_H = int(input('Enter number of Hydrogen Atoms: '))
Enter number of Hydrogen Atoms: 4
No_C = int(input('Enter number of Carbon Atoms: '))
Enter number of Carbon Atoms: 3
No_O = int(input('Enter number of Oxygen Atoms: '))
Enter number of Oxygen Atoms: 10
#Printing Molecular Weight
print('Molecular weight of compound is:', (No_H * 1.00794) + (No_C * 12.0107) + (No_O * 15.9994), 'grams/mole')
Molecular weight of compound is: 200.05786 grams/mole
