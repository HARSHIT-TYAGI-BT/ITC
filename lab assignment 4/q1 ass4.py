Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#question 1
#input marks:

Marks = float(input('Enter your Marks: '))
Enter your Marks: 75
if Marks<25 :
    print('Your Grade is F')
elif 25<=Marks<45 :
    print('Your Grade is E')
elif 45<=Marks<50 :
    print('Your Grade is D')
elif 50<=Marks<60 :
    print('Your Grade is C')
elif 60<=Marks<80 :
    print('Your Grade is B')
elif Marks>=80 :
    print('Your Grade is A')
else:
     print('Invalid Marks')