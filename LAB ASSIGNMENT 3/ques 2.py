Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
b = float(input('Enter first number: '))
Enter first number: 44
a = input('Enter sign(+, -, *, / or q for quit): ')
Enter sign(+, -, *, / or q for quit): +
while (a!='q'):
    if a=='+':
        b = b + float(input('Next number: '))
    elif a == '-':
        b = b - float(input('Next number: '))
    elif a == '*':
        b = b * float(input('Next number: '))
    elif a == '/':
        b = b / float(input('Next number: '))
    else:
        print('Invalid operator, try again')
    a = input('Enter next sign(+, -, *, / or q for quit): ')

    
Next number: 33
Enter next sign(+, -, *, / or q for quit): -
Next number: 44
Enter next sign(+, -, *, / or q for quit): q

print(b)
33.0
