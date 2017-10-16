with open('files/write.txt', 'w') as write_file:
    write_file.write('Hello Hello Ninjas, This is an example of writing to file')
    write_file.write('\nand this is a second line')

with open('files/write.txt', 'a') as write_file:
    write_file.write('\nAmending the third line')
    

quotes = [
    '\nHello, This is an example of python writing files',
    '\nAmending a second line',
    '\nand finally ending it with the third'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
