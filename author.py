class Author:
    def __init__(self, name):
        self.name = name
        self.list = []

    ##this is a method in python classes that can return usefull information when the class instance is printed
    def __str__(self):
        titles = ','.join(self.list) or 'No Published Books'
        return f'{self.name}, Books: {titles}'

    def addBook(self, book):
        self.list.append(book)

author = Author('Roald Dahl')

author.addBook('James and The Giant Peach')
author.addBook('Charlie and THe Chocolate Factory')

print(author)
