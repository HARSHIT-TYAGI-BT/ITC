print('Question-1')
text = 'Python is a case sensitive language'
# a.
print('Lenght of string is',len(text))
# b.
print(text[::-1])
# c.
new_text = text[12:26]
print(new_text)
# d.
print(text.replace('a case sensitive', 'an object oriented'))
# e.
print('Index of "a" in original string is', text.find('a'))
# f.
print(text.replace(' ', ''))
print()


print('Question-2')
Name = 'ABC'
SID = '2110xxxx'
Branch = 'XYZ'
CGPA = '9.9'

paragraph = 'Hey, {} Here!\nMy SID is {}\nI am from {} Department and my CGPA is {}'

# String Formatting
print(paragraph.format(Name,SID,Branch,CGPA))
print()


print('Question-3')
a = 56
b = 10

print('a & b =',a & b)
print('a | b =',a | b)
print('a ^ b =',a ^ b)
print('a << 2 =', (a << 2), 'and', 'b << 2 =', (b << 2))
print('a >> 2 =', (a >> 2), 'and', 'b >> 4 =', (b >> 4))
print()


print('Question-4')
string = str(input('Enter String: '))

if 'name' in string:
    print('Yes')
else:
    print('No')
print()


print('Question-5')
Side1 = int(input('Enter First side: '))
Side2 = int(input('Enter Second side: '))
Side3 = int(input('Enter Third side: '))

# Using Logical Operators as a Conditional Statement:
test = (Side1+Side2>Side3) and (Side2+Side3>Side1) and (Side1+Side3>Side2)
test and print('Yes(Triangle Possible)')
test or print('No(Triangle not Possible)')
print()


print('Question-6')
a1 = int(input('Enter first number: '))
b1 = int(input('Enter second number: '))

c = a1^b1
c = bin(c)

print("Number of bits that need to be flipped =", c.count('1'))
