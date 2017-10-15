def cough_dec(func):
    
    def cough_wrapper():
        #code before function
        print('*cough*')
        func()
        #code after function
        print('*cough*')
    return cough_wrapper

@cough_dec
def discount():
    print('Can you give me a discount?')

@cough_dec
def answer():
    print('it\'s only 50 cents dear...')

discount()
answer()