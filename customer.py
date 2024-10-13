from rental import Rental

class Customer:
    """A customer who rents movies."""

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer."""
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self) -> str:
        """Get the customer's name."""
        return self.name

    def statement(self) -> str:
        """Create a statement of rentals for the current period."""
        statement = f"Rental Report for {self.name}\n\n"
        header_fmt = "{:40s}  {:6s} {:6s}\n"
        statement += header_fmt.format("Movie Title", "  Days", " Price")
        rental_fmt = "{:40s}  {:6d} {:6.2f}\n"

        for rental in self.rentals:
            statement += rental_fmt.format(
                rental.get_movie().get_title(),
                rental.get_days_rented(),
                rental.get_price())

        # footer: summary of charges
        statement += "\n"
        statement += "{:40s}  {:6s} {:6.2f}\n".format(
            "Total Charges", "", self.total_amount())
        statement += "Frequent Renter Points earned: {}\n".format(
            self.total_rental_points())

        return statement

    def total_amount(self) -> float:
        return sum([rental.get_price() for rental in self.rentals])

    def total_rental_points(self) -> int:
        return sum([rental.get_rental_points() for rental in self.rentals])
