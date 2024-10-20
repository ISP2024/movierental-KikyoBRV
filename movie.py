import csv
from calendar import month
from typing import Collection
from dataclasses import dataclass

class MovieCatalog:
    _instances = None

    def __new__(cls):
        """Create a new MovieCatalog if not already exist."""
        if cls._instances is None:
            cls._instances = super(MovieCatalog, cls).__new__(cls)
            cls._instances._movie_list = cls.load_movie_data()
        return cls._instances

    @staticmethod
    def load_movie_data():
        """Load movie data from a CSV file."""
        movies = []
        with open("movies.csv", encoding="utf-8") as movie_file:
            movie_reader = csv.DictReader(movie_file)
            next(movie_reader)
            for _, movie_data in enumerate(movie_reader):
                try:
                    movie = Movie(
                        movie_data['title'],
                        int(movie_data['year']),
                        movie_data['genres'].split('|')
                    )
                    movies.append(movie)
                except (TypeError, ValueError):
                    continue

        return movies

    def get_movie(self, title, year=None):
        for movie in self._movie_list:
            if title.lower() == movie.title.lower() and (not year or year == movie.year):
                return movie

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