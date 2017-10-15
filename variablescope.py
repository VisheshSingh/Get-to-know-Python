# VARIABLE SCOPE

# GLOBAL VARIABLE
my_name = 'ryu'

def printname():
    # overriding global variable
    global my_name
    # LOCAL VARIABLE
    my_name = 'yoshi'
    print('name inside function is: ', my_name)

printname()
print('name outside function is: ', my_name)