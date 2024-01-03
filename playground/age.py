#!/usr/bin/python3
age = eval(input('Enter age: '))
if age < 5:
    print('Too young for school')
elif age == 5:
    print('Go to Kindergarten')
elif (age > 5) and (age <= 17):
    grade = age - 5
    print('Go to {} grade'.format(grade))
else:
    print('go to college')
