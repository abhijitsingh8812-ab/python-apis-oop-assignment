"""Q02 — OOP: Encapsulation"""
class Book:
    def __init__(self, title: str, author: str, price: float, discount: float = 0.1):
        self.title = title
        self.author = author
        self.price = float(price)
        # "private" attribute by convention
        self._discount = 0.0
        self.discount = discount  # use setter validation

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float) -> None:
        try:
            v = float(value)
        except Exception:
            raise ValueError("Discount must be a number between 0.0 and 0.9")
        if not (0.0 <= v <= 0.9):
            raise ValueError("Discount must be between 0.0 and 0.9")
        self._discount = v

    def get_price_after_discount(self) -> float:
        return round(self.price * (1 - self._discount), 2)

    def __str__(self) -> str:
        return f"{self.title} by {self.author} — Price: {self.price} (discount: {self._discount})"

if __name__ == "__main__":
    b = Book("Python Tricks", "Dan Bader", 399.0)
    print(b)
    print("Price after default discount:", b.get_price_after_discount())
    # set discount via setter
    b.discount = 0.2
    print("Price after 20% discount:", b.get_price_after_discount())
