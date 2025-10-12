# book_class.py

class Book:
    """A class representing a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation of the Book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Print a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")
