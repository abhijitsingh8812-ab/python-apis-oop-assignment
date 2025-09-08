"""Q04 — OOP: Polymorphism (duck typing)"""
class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = float(price)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size_mb: float):
        super().__init__(title, author, price)
        self.file_size_mb = float(file_size_mb)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, File Size: {self.file_size_mb}MB"


def print_details(obj):
    # duck-typing: assume the object has get_details()
    try:
        print(obj.get_details())
    except AttributeError:
        print(str(obj))


if __name__ == "__main__":
    items = [
        Book("Sapiens", "Yuval Harari", 399.0),
        EBook("Atomic Habits", "James Clear", 199.0, 1.8),
        Book("Zero to One", "Peter Thiel", 349.0),
    ]

    for it in items:
        print_details(it)
