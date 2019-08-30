num = [1,2,3]
##this is a list comprehension which is a usefull way in modern python to limit the amount of code you write
## there is a miniture for loop in the array
newNum = [num + 1 for num in num ]

print(newNum)

##this is a list comprehension which is a usefull way in modern python to limit the amount of code you write
## there is a miniture for loop in the array
classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 29']

itecClasses = [classes for classes in classes if 'ITEC' in classes]

print(itecClasses)