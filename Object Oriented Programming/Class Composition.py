class BookShelf:

    def __init__(self, *books):
        self.Books = books

    def __str__(self):
        return f"BookShelf has {len(self.Books)} books."


class Book:
    def __init__(self,name):
        self.Name = name

    def __str__(self):
        return f'Book name is "{self.Name}".'

book1 = Book("Make in India")
book2 = Book("India is the best")

shelf = BookShelf(book1,book2)
print(shelf)

