# SORTING

nums = [1,1,2,7,8,6,7,0,4,3,9,2]
print(sorted(nums)) # [0, 1, 1, 2, 2, 3, 4, 6, 7, 7, 8, 9]

names = ["vish", "shaun", "Abe","Brain" , "ape", "xixin"]
print(sorted(names)) #['Abe', 'Brain', 'ape', 'shaun', 'vish', 'xixin']

# SETS - A COLLECTION OF DATA THAT DO NOT CONTAIN DUPLICATE VALUES
print(set(nums)) #{0, 1, 2, 3, 4, 6, 7, 8, 9}

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

def belt_count(dict):
    belts = list(dict.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

belt_count(ninja_belts)
