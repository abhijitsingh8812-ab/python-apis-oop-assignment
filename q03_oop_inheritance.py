"""Q03 — OOP: Inheritance"""
class Book:
    def __init__(self, title: str, author: str, price: float, discount: float = 0.0):
        self.title = title
        self.author = author
        self.price = float(price)
        self._discount = float(discount)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

    def get_price_after_discount(self) -> float:
        return round(self.price * (1 - self._discount), 2)


class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size_mb: float, discount: float = 0.0):
        super().__init__(title, author, price, discount)
        self.file_size_mb = float(file_size_mb)

    def get_details(self) -> str:
        base = super().get_details()
        return f"{base}, File Size: {self.file_size_mb}MB"


if __name__ == "__main__":
    eb = EBook("Deep Learning", "Ian Goodfellow", 799.0, 2.5, discount=0.15)
    print(eb.get_details())
    print("Discounted price:", eb.get_price_after_discount())
