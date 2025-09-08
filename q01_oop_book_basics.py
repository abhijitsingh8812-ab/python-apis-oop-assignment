"""Q01 — OOP: Class & Object Basics"""
class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = float(price)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

if __name__ == "__main__":
    books = [
        Book("1984", "George Orwell", 299.0),
        Book("Clean Code", "Robert C. Martin", 499.0),
        Book("The Pragmatic Programmer", "Andrew Hunt", 599.0),
    ]

    for b in books:
        print(b.get_details())
