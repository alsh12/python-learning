class Book:
    Types = ("HardCover","PaperBack")

    def __init__(self,name,bookType,weight):
        self.Name = name
        self.BookType = bookType
        self.Weight = weight

    def __repr__(self):
        return f"<{self.BookType} Book {self.Name} has weight up to {self.Weight} in grams>"

    @classmethod
    def HardCover(cls,name,bookWeight):
        return cls(name,cls.Types[0],bookWeight + 200)

    @classmethod
    def PaperBack(cls,name,bookWeight):
        return cls(name,cls.Types[1],bookWeight)

hardCoverBook = Book.HardCover("Deep Learning",2000)
paperBackBook = Book.PaperBack("Python Programming",800)

print(hardCoverBook)
print(paperBackBook)
