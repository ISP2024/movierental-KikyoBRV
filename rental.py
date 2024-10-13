from movie import Movie
import logging

class Rental:
    """A rental of a movie by a customer."""

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        """Get the rented movie."""
        return self.movie

    def get_days_rented(self):
        """Get the number of days the movie has been rented."""
        return self.days_rented

    def get_price(self) -> float:
        """Calculate the price for this rental."""
        amount = 0
        if self.movie.get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 per day.
            amount = 2.0
            if self.days_rented > 2:
                amount += 1.5 * (self.days_rented - 2)
        elif self.movie.get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 per day.
            amount = 1.5
            if self.days_rented > 3:
                amount += 1.5 * (self.days_rented - 3)
        elif self.movie.get_price_code() == Movie.NEW_RELEASE:
            # Straight $3 per day charge.
            amount = 3 * self.days_rented
        else:
            log = logging.getLogger()
            log.error(f"Movie {self.movie} has unrecognized priceCode {self.movie.get_price_code()}")
        return amount
