question = int(input('Enter the amount of classes you are taking: '))
##get number of classes
list = []
for num in range(question):
    ##asks user for each class and appends it to list
    classes = input('Enter class name: ')
    list.append(classes)

print('These are the classes you are taking;')
#prints the list out
for c in list:
    print(c)
    