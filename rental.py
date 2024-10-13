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
        """Delegates to the movie to get the price."""
        return self.movie.get_price(self.days_rented)

    def get_rental_points(self) -> int:
        """Delegates to the movie to get the rental points."""
        return self.movie.get_rental_points(self.days_rented)
