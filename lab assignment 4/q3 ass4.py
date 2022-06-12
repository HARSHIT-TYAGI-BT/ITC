Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#question 3
import random

for i in range(1,11):
     a=random.randint(1,10)
     b=random.randint(1,10)
     print('Question', i, ':', a, '*', b, '= ??')
     answer=int(input('Enter answer: '))
     if answer==a*b:
          print('Right!')
     elif answer!=a*b:
          print('Wrong. The answer is', a*b)
     print()