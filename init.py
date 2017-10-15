# CLASSES

class Planet:

    def __init__(self, name = 'anonymous', radius='unknown', gravity="not-determined", system='Planet-0'):
        self.name = name,
        self.radius = radius,
        self.gravity = gravity,
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting the {self.system}'

hoth = Planet()

print(f'Name of the planet: {hoth.name}')
print(f'Radius of the planet: {hoth.radius}')
print(f'Gravity of the planet: {hoth.gravity}')
print(hoth.orbit())

naboo = Planet('naboo', 450000, 2.6, 'naboo system')
print(f'Name of the planet: {naboo.name}')
print(f'Radius of the planet: {naboo.radius}')
print(f'Gravity of the planet: {naboo.gravity}')
print(naboo.orbit())

