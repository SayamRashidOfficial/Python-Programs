class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nPrice: Rs.{self.price:.2f}"

book1 = Book("Python Programming", "sayam", 300, 29.99)
book2 = Book("Machine Learning", "hamad", 450, 39.95)

print("Book 1 Details:")
print(book1)

print("\nBook 2 Details:")
print(book2)

