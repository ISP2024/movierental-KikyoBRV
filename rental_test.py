import unittest
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        # Create sample movies with title, year, and genres
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2021, ["Drama", "History"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children", "Animation"])

    def test_movie_attributes(self):
        """Test to ensure movie attributes are correctly set."""
        movie = Movie("Air", 2021, ["Drama", "History"])
        self.assertEqual("Air", movie.get_title())
        self.assertEqual(2021, movie.year)
        self.assertIn("Drama", movie.genres)

    def test_rental_price(self):
        """Test price calculation for different movie categories and rental durations."""
        # Test new release movie pricing
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        # Test regular movie pricing
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)

        # Test children's movie pricing
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """Test frequent renter points calculation."""
        # Test for new release movies
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

        # Test for regular movies
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_rental_points(), 1)

        # Test for children's movies
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
