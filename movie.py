from typing import Collection

from dataclasses import dataclass

@dataclass(frozen=True)
class Movie:
    """A movie that can be rented."""

    title: str
    year: int
    genres: Collection[str]

    def get_title(self) -> str:
        """Get the title of the movie."""
        return self.title

    def is_genre(self, string: str) -> bool:
        """Check if the string is in a collection of genres"""
        return string.lower() in self.genres

    def __str__(self) -> str:
        return f" {self.title} ({self.year})"