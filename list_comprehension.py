list = [5, 10, 50, 100, 1000]

dbl_list = []
for n in list:
    dbl_list.append(n*2)
print(dbl_list)

#COMPREHENSION METHOD
dbl_list = [n*2 for n in list]
print(dbl_list)

#SQUARING NUMBERS
nums = [1,2,3,4,5,6,7,8,9,10]
squared_even=[]

for num in nums:
    if(num**2 % 2 == 0):
        squared_even.append(num**2)
print(squared_even)

#COMPREHENSION METHOD
squared_even_nums = [num**2 for num in nums if(num**2 % 2 == 0)]
print(squared_even_nums)