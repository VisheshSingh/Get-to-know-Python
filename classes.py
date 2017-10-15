# CLASSES

class Planet:

    def __init__(self):
        self.name = 'Hoth',
        self.radius = 200000,
        self.gravity = 5.5,
        self.system = "Hoth system"

    def orbit(self):
        return f'{self.name} is orbiting the {self.system}'

hoth = Planet()

print(f'Name of the planet: {hoth.name}')
print(f'Radius of the planet: {hoth.radius}')
print(f'Gravity of the planet: {hoth.gravity}')

