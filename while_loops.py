#WHILE LOOPS

age = 25
num = 0

# Print numbers from 0 to 24
# while num < age:
#     print(num)
#     num += 1

# Print even numbers from 0 to 24
# while num < age:
#     if(num % 2 == 0):
#         print(num)
#     num += 1

# Print even numbers and break if it reaches 10
while num < age:
    if num == 0:
        num += 1
        continue
    if(num % 2 == 0):
        print(num)
    if(num == 10):
        break
    num += 1
