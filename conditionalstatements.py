# Program:      Conditional statements in Python
# Programmer:   Sammit Jain | 2014B4A3909G

print('Enter your name: ')
myName = input()
print('Let''s assign you a grade shall we?')
score = input('What was your GPA last sem? ')
score = int(score)
if score<=2:
    print('You deserve an E')
elif score <=5:
    print('You deserve a C')
elif score <=8:
    print('Decent, you get a B')
else:
    print('At least be honest with a computer program.')

