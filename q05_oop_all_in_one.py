"""Q05 — OOP: All-in-One (Price, Book, Inventory)"""
from typing import List

class Price:
    def __init__(self, value: float, currency: str = "INR"):
        try:
            v = float(value)
        except Exception:
            raise ValueError("Price value must be numeric")
        if v < 0:
            raise ValueError("Price cannot be negative")
        self.value = round(v, 2)
        self.currency = str(currency)

    def __repr__(self) -> str:
        return f"{self.currency} {self.value:.2f}"

    def __str__(self) -> str:
        return self.__repr__()


class Book:
    def __init__(self, title: str, author: str, price: Price):
        self.title = str(title)
        self.author = str(author)
        if not isinstance(price, Price):
            raise TypeError("price must be a Price instance")
        self.price = price

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title.lower(), self.author.lower()) == (other.title.lower(), other.author.lower())

    @classmethod
    def from_dict(cls, d: dict):
        title = d.get("title")
        author = d.get("author")
        if title is None or author is None:
            raise ValueError("dict must contain 'title' and 'author'")
        price_val = d.get("price", 0)
        currency = d.get("currency", "INR")
        price = Price(price_val, currency)
        return cls(title, author, price)

    def __str__(self) -> str:
        return f"{self.title} by {self.author} — {self.price}"


class Inventory:
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self._books.append(book)

    def remove_book(self, title: str, author: str) -> bool:
        for i, b in enumerate(self._books):
            if b.title.lower() == title.lower() and b.author.lower() == author.lower():
                del self._books[i]
                return True
        return False

    def find_by_author(self, author: str) -> List[Book]:
        return [b for b in self._books if b.author.lower() == author.lower()]

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __str__(self) -> str:
        if not self._books:
            return "Inventory is empty"
        return "\n".join(str(b) for b in self._books)


if __name__ == "__main__":
    raw = [
        {"title": "Clean Architecture", "author": "Robert C. Martin", "price": 549.0},
        {"title": "Refactoring", "author": "Martin Fowler", "price": 699.5, "currency": "INR"},
        {"title": "Design Patterns", "author": "Erich Gamma", "price": 459.0},
    ]

    inv = Inventory()
    for d in raw:
        b = Book.from_dict(d)
        inv.add_book(b)

    print("All books in inventory:")
    print(inv)

    # remove one
    inv.remove_book("Refactoring", "Martin Fowler")
    print('\nAfter removing Refactoring:')
    print("Inventory size:", len(inv))

    print('\nBooks by Robert C. Martin:')
    for b in inv.find_by_author("Robert C. Martin"):
        print(b)
