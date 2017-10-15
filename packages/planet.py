# CLASSES

class Planet:
    #class level attributes
    shape = 'round'

    #INSTANCE ATTRIBUTES
    def __init__(self, name = 'anonymous', radius='unknown', gravity="not-determined", system='Planet-0'):
        self.name = name,
        self.radius = radius,
        self.gravity = gravity,
        self.system = system

    #INSTANCE METHOD
    def orbit(self):
        return f'{self.name} is orbiting the {self.system}'

    #CLASS METHODS
    @classmethod 
    def commons(cls):
        return f'All planets are {cls.shape}'

    #STATIC METHODS - only has access to parameters we send in and not self or class level methods or attrs
    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planets spins and spins at {speed}'


# hoth = Planet()

# print(f'Name of the planet: {hoth.name}')
# print(f'Radius of the planet: {hoth.radius}')
# print(f'Gravity of the planet: {hoth.gravity}')
# print(hoth.orbit())

naboo = Planet('naboo', 450000, 2.6, 'naboo system')
print(f'Name of the planet: {naboo.name}')
print(f'Radius of the planet: {naboo.radius}')
print(f'Gravity of the planet: {naboo.gravity}')
print(naboo.orbit())
#print(hoth.shape)
print(naboo.shape)

print(Planet.commons())
print(naboo.commons())

print(Planet.spin())
print(naboo.spin('a very high speed'))