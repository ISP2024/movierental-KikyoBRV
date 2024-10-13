from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(PriceStrategy, cls).__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days):
        """Price for new releases is $3 per day."""
        return 3 * days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_rental_points(self, days):
        """Regular rentals earn 1 point regardless of days rented."""
        return 1

    def get_price(self, days):
        """Two days for $2, additional days $1.50 per day."""
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_rental_points(self, days):
        """Children's rentals earn 1 point regardless of days rented."""
        return 1

    def get_price(self, days):
        """Three days for $1.50, additional days $1.50 per day."""
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount


# Define instances of the strategies as named constants
NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()


class Movie:
    """A movie that can be rented."""

    REGULAR = REGULAR
    CHILDRENS = CHILDREN
    NEW_RELEASE = NEW_RELEASE

    def __init__(self, title: str, price_strategy: PriceStrategy):
        self.title = title
        self.price_strategy = price_strategy

    def get_price(self, days: int) -> float:
        return self.price_strategy.get_price(days)

    def get_rental_points(self, days: int) -> int:
        return self.price_strategy.get_rental_points(days)

    def get_title(self) -> str:
        return self.title

    def get_price_code(self):
        return self.price_strategy
