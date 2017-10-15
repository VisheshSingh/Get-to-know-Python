# STRINGS

greet = 'hello'

print(greet[0]) #h
print(greet[1]) #e
print(greet[-1]) #0
print(greet[-5]) #h

print(greet[0:3]) #hel - 3 is not inclusive

str2 = 'dudes!'

print(greet + ' ' + str2) #hello dudes!

print(greet * 3) #hellohellohello


# STRING METHODS
print(greet.upper()) #HELLO

animals = 'cats, dogs, tiger, birds'
print(animals.split(',')) #['cats', ' dogs', ' tiger', ' birds']

print(len(animals)) #24