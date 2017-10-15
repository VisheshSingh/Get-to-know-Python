# FOR LOOPS

users = ['ryu', 'yoshi', 'jim', 'chan']

# for user in users: 
#     print(user)

# for user in users[1:3]: 
#     print(user)

for user in users:
    if user == 'yoshi':
        print(f'{user} - black belt')
        break
    else:
        print(user)