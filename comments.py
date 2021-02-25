num = 2

if num%2 == 0:
    print("It is Even")
else:
    print("It is odd")

"This line will be ignored"
print("Pylenin loves Python")
"""
Bigger comments can be written
over multiple lines.
This is a multi-line comment.
"""
print("Pylenin loves Python")


def addition(x,y):
    """Takes x and y and returns their sum"""
    return x+y

print(addition.__doc__)


class Person:
    """Stores the name, age and country of a person"""
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

print(Person.__doc__)

y = type("Lenin")


# initialisation
a = 10
b = 12
c = 13

# equation
s = (a + b + c) / 2

# calcul de l'aire du triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
""" formule de l'aire d'une triangle"""
print('The area of our triangle is %0.2f' %area)




a = float(input('Enter 1st side: '))
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of our triangle is %0.2f' %area)

print('fin de journee')