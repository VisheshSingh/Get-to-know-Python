# DICTIONARIES

ninja = {"crystal": "red", "yoshi": "black"}

print(ninja["crystal"]) # red

"yoshi" in ninja # true
"ken"  in ninja # false

print(ninja.keys()) # dict_keys(['crystal', 'yoshi'])
print(list(ninja.keys())) # ['crystal', 'yoshi']

print(ninja.values())

vals = list(ninja.values())
print(vals)

print(vals.count('red')) # 1
print(vals.count('blue')) # 0

ninja["ken"] = "blue"
print(ninja)

person = dict(name="fu", age=12)
print(person)

# PUTTING DICTIONARIES TO USE
ninja_belts = {}

while True:
    name=input('enter a name:')
    belt=input('enter a belt:')
    ninja_belts[name] = belt

    another_input = input('Do you want to enter another one (y/n):')
    if(another_input == 'y'):
        continue
    else:
        break

def ninja_dict(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_dict(ninja_belts)