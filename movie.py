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
