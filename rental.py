from pricing import PriceStrategy,NewRelease,RegularPrice,ChildrensPrice

NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()

class Rental:
    """A rental of a movie by a customer."""

    def __init__(self, movie, days_rented, price_code: PriceStrategy):
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

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

