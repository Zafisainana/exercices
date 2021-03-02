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


"""

a = float(input('Enter 1st side: '))
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))

"""

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of our triangle is %0.2f' %area)

print('fin de journee')

countries = []
temperatures = []

countries.append('France')
countries.append('Spain')
countries.append('Canada')


temperatures.append(122.5)
temperatures.append(124)
temperatures.append(105.5)


print(countries)
print(temperatures)


france = countries[0]
france_temperature = temperatures[0]

print(france, france_temperature, sep='/')


fusion = [countries[0], temperatures[0], countries[1], temperatures[1], countries[2], temperatures[2]]

print(fusion)

# longueur d'une liste
# len

int_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
total_lenght = len(int_months)

print('longueur total est: ', total_lenght)

last_value_position = len(int_months) - 1
last_value = int_months[last_value_position]

print(last_value)


countries = []
temperatures = []

countries = ['France', 'Spain', 'US', 'Canada', 'Australia', 'Argentina']
temperatures = [112.5, 124.0, 134.1, 105.2, 112.5, 128.3]

countries_slice = countries[0:3]
temperatures_slice = temperatures[len(temperatures)-4:] #meilleur choix

print(countries_slice)
print(temperatures_slice)