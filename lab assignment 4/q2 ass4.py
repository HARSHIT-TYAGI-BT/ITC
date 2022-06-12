Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#QUESTON 2
# Input Year:
year = int(input('Enter Year: '))
Enter Year: 2300
if year % 100 == 0:
     if year % 400 ==0:
          print('Leap Year')
     else:
          print('Not Leap')
else:
    if year % 4 == 0:
         print('Leap Year')
    else:
         print('Not Leap')
         