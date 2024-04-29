class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

class Magazine:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

    def __len__(self):
        return self.pages

book = Book("Harry Potter", "J.K. Rowling", 400)
magazine = Magazine("National Geographic", "National Geographic Society", 50)

print(len(book))
print(len(magazine))
