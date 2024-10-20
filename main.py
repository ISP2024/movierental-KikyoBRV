# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from movie import Movie, MovieCatalog

def make_movies():
    """Some sample movies."""
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Young Woman and the Sea"),
        catalog.get_movie("Cinderella"),
        catalog.get_movie("Son of Saul"),
        catalog.get_movie("Air"),
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        if movie:
            customer.add_rental(Rental(movie, days))
            days = (days + 2) % 5 + 1
        else:
            print(f"Sorry, couldn't find that movie.")
    print(customer.statement())

