from typing import Collection

from pricing import PriceStrategy,NewRelease,RegularPrice,ChildrensPrice

# Define instances of the strategies as named constants
NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()


class Movie:
    """A movie that can be rented."""

    REGULAR = REGULAR
    CHILDRENS = CHILDREN
    NEW_RELEASE = NEW_RELEASE

    def __init__(self, title: str, year: int, genre: Collection[str]):
        self.title = title
        self.year = year
        self.genre = genre

    def get_title(self) -> str:
        return self.title

    def is_genre(self, string: str) -> bool:
        return string.lower() in self.genre

    def __str__(self) -> str:
        return f" {self.title} ({self.year})"