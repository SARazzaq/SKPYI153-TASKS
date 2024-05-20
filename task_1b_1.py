class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._copies_sold = 0

    # Getter and setter methods for title
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    # Getter and setter methods for author
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value

    # Getter and setter methods for publisher
    @property
    def publisher(self):
        return self._publisher
    
    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    # Getter and setter methods for price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    # Getter and setter methods for copies sold
    @property
    def copies_sold(self):
        return self._copies_sold
    
    @copies_sold.setter
    def copies_sold(self, value):
        self._copies_sold = value

    # Method to calculate royalty
    def royalty(self):
        if self._copies_sold <= 500:
            return 0.10 * self._price * self._copies_sold
        elif self._copies_sold <= 1500:
            return (0.10 * self._price * 500) + (0.125 * self._price * (self._copies_sold - 500))
        else:
            return (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (self._copies_sold - 1500))


class Ebook(Book):
    def __init__(self, title, author, publisher, price, format):
        super().__init__(title, author, publisher, price)
        self._format = format

    # Getter and setter methods for format
    @property
    def format(self):
        return self._format
    
    @format.setter
    def format(self, value):
        self._format = value

    # Override royalty method to deduct GST
    def royalty(self):
        base_royalty = super().royalty()
        gst_deduction = 0.12 * base_royalty
        return base_royalty - gst_deduction

# Example usage
book = Book("Python Programming", "John Doe", "Tech Books", 50)
book.copies_sold = 2000
print(f"Book Royalty: {book.royalty()}")

ebook = Ebook("Python Programming", "John Doe", "Tech Books", 50, "EPUB")
ebook.copies_sold = 2000
print(f"Ebook Royalty: {ebook.royalty()}")
