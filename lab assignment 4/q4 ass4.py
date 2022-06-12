Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#question 4
# Start from 1 and into a while loop:
a=1

while a<200:
    if (a%5 == 2) and (a%6 == 3) and (a%7 == 2):
        print('No. of Candies =',a)
    a+=1