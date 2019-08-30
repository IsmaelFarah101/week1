num = [1,2,3]

newNum = [num + 1 for num in num ]

print(newNum)

classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 29']

itecClasses = [classes for classes in classes if 'ITEC' in classes]

print(itecClasses)