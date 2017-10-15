# LISTS

str = "hello there dudes"
print(str.split(' '))  #['hello', 'there', 'dudes']

fib1 = [0, 1, 1, 2, 3, 5, 8, 13]
fib2 = [21, 34, 55]

print(fib1[4])  #3
print(fib1[7]) #13
print(fib1[-1])  #13

print(fib1[0:4]) #[0, 1, 1, 2]
print(fib1 + fib2) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fib = fib1 + fib2
fib.append(89)
print(fib) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#fib.pop()
fib.remove(89) 
print(fib) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#del(fib[3]) # 2 will be deleted

characters = ['mario', 'luigi', 'bowser']

nums = [characters, fib1, 5, 25, 'hello', fib2]
print(nums) #[['mario', 'luigi', 'bowser'], [0, 1, 1, 2, 3, 5, 8, 13], 5, 25, 'hello', [21, 34, 55]]

print(nums[0]) #['mario', 'luigi', 'bowser']
print(nums[1][5]) #5