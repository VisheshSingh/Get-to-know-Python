# FUNCTIONS

def greet():
    print('hello world!')

greet()

name = input('enter your name: ')
time = input('enter your time (morning, afternoon, evening, night): ')

def greeting(name= 'anonymous', time= 'morning'):
    print(f'Hello {name}, have a good {time}!')

greeting(name, time)

greeting()

# AREA OF CIRCLE
radius = int(input('Enter a radius: '))
def area(radius):
    return (3.142 * radius ** 2)

# VOLUME OF CYLINDER
length = int(input('enter a length: '))
def vol(area, length):
    print(area * length)

area_calc = area(radius)
vol(area_calc, length)