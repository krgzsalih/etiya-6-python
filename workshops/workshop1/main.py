userList = []
# wants to user enter name for 10 times and
# push the inputs values to the an empty array
for name in range(10):
    print('Enter your name:')
    name = input()
    userList.append(name)

print('User list : ')

# prints the names in the array
for i in userList:
    print(i)
