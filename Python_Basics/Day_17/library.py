class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} has been borrowed successfully."
        else:
            return f"{self.title} is already borrowed."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is already available."

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def borrow(self):
        return f"{self.title} is available to download. Enjoy!!!!!"

book1 = Book('How to get a job', 'CHATGPT PRO MAX ULTRA')
book2 = Book('How to get a bigger job than ChatGPT', 'CLAUDE PRO MAX')
book3 = Book('How to get attention', 'GROK')
ebook1 = EBook("Python for Beginners", "Apil", 5)

print(book1.borrow())
print(book2.return_book())
print(book3.borrow())
print(book1.return_book())
print(book1.borrow())

print(ebook1.borrow())
print(ebook1.borrow())
print(ebook1.file_size, "MB")

