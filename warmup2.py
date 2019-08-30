question = int(input('Enter the amount of classes you are taking: '))
list = []
for num in range(question):
    classes = input('Enter class name: ')
    list.append(classes)

print('These are the classes you are taking;')
for c in list:
    print(c)
    