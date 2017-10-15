from init import Planet
from packages.calc import planet_mass, planet_vol

naboo = Planet('naboo', 450000, 2.6, 'naboo system')
print(f'Name of the planet: {naboo.name}')
print(f'Radius of the planet: {naboo.radius}')
print(f'Gravity of the planet: {naboo.gravity}')

mass = planet_mass(5.5, 5000)
vol = planet_vol(14050)

print(mass)
print(vol)

print(f'the planet\'s mass is {mass} and vol is {vol}')
