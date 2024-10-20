import csv
import logging
from typing import Collection
from dataclasses import dataclass

logging.basicConfig(level=logging.ERROR, filename="logging.txt", filemode="w")
LOGGER = logging.getLogger("error_log")
LOGGER.addHandler(logging.StreamHandler())

class MovieCatalog:
    __instances = None

    def __new__(cls):
        """Create a new MovieCatalog if not already exist."""
        if cls.__instances is None:
            cls.__instances = super(MovieCatalog, cls).__new__(cls)
            cls.__instances._movie_list = cls.__load_movie_data()
        return cls.__instances

    @staticmethod
    def __load_movie_data():
        """Load movie data from a CSV file."""
        movies = []
        with open("movies.csv", encoding="utf-8") as movie_file:
            movie_reader = csv.DictReader(movie_file)
            next(movie_reader)
            for line_number, movie_data in enumerate(movie_reader):
                try:
                    movie = Movie(
                        movie_data['title'],
                        int(movie_data['year']),
                        movie_data['genres'].split('|')
                    )
                    movies.append(movie)
                except (TypeError, ValueError):
                    format_msg = ",".join(
                        str(value) for key, value in movie_data.items()
                        if key != 'id' and value is not None)
                    logging.error('Line %d: Unrecognized format "%s"',
                                  line_number + 1, format_msg)
                    continue

        return movies

    def get_movie(self, title, year=None):
        """Get movie by title and year."""
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