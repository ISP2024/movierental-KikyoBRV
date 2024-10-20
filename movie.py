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


    def get_title(self) -> str:
        return self.title
