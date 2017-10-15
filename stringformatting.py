# STRING FORMATTING

radius = int(input("Enter the radius: "))
area = 3.142 * radius ** 2
print('The area of circle with radius =', radius,'is', area)

num1 = 3.14258973
num2 = 2.95470314

#PREVIOUS METHOD
print('num1 is', num1, 'and num2 is', num2) # num1 is 3.14258973 and num2 is 2.95470314

#FORMAT METHOD
print('num1 is {0} and num2 is {1}'.format(num1, num2))
print('num1 is {0:.2} and num2 is {1:.3}'.format(num1, num2))
print('num1 is {0:.2f} and num2 is {1:.3f}'.format(num1, num2))

# num1 is 3.14258973 and num2 is 2.95470314
# num1 is 3.1 and num2 is 2.95
# num1 is 3.14 and num2 is 2.955

#USING f-STRINGS
print(f'num1 is {num1} and num2 is {num2}')
print(f'num1 is {num1:.4} and num2 is {num2:.3}')
print(f'num1 is {num1:.4f} and num2 is {num2:.3f}')

# num1 is 3.14258973 and num2 is 2.95470314
# num1 is 3.143 and num2 is 2.95
# num1 is 3.1426 and num2 is 2.955