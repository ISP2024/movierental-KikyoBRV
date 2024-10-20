from datetime import datetime

from pricing import NewRelease,RegularPrice,ChildrensPrice

NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()

class Rental:
    """A rental of a movie by a customer."""

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = self.price_code_for_movie(movie)

    @classmethod
    def price_code_for_movie(cls, movie):
        """Determine the price code for a movie based on its release year and genres."""
        current_year = datetime.now().year

        # Check if the movie was released this year
        if movie.year == current_year:
            return NewRelease()

        # Check if the movie is a children's movie based on genres
        if "Children" in movie.genres:
            return ChildrensPrice()

        # Otherwise, it's a regular priced movie
        return RegularPrice()

    def get_movie(self):
        """Get the rented movie."""
        return self.movie

    def get_days_rented(self):
        """Get the number of days the movie has been rented."""
        return self.days_rented

    def get_price(self) -> float:
        """Delegates to the movie to get the price."""
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self) -> int:
        """Delegates to the movie to get the rental points."""
        return self.price_code.get_rental_points(self.days_rented)

    def get_price_code(self):
        return self.price_code
