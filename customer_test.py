import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2024, ["Action", "Adventure"])
        self.regular_movie = Movie("CitizenFour", 2014,
                                   ["Documentary", "Thriller"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children", "Animation"])

    @unittest.skip("No convenient way to test")
    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])

        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_amount(self):
        # Initially no rentals
        self.assertEqual(self.c.total_amount(), 0)

        # Add rentals
        rental1 = Rental(self.new_movie, 4)
        rental2 = Rental(self.regular_movie, 5)
        rental3 = Rental(self.childrens_movie, 4)
        self.c.add_rental(rental1)
        self.c.add_rental(rental2)
        self.c.add_rental(rental3)

        expected_total = 12.0 + 6.5 + 3.0
        self.assertEqual(self.c.total_amount(), expected_total)

    def test_total_rental_points(self):
        # No rentals yet
        self.assertEqual(self.c.total_rental_points(), 0)

        # Add a new release rental (4 days)
        self.c.add_rental(Rental(self.new_movie, 4))
        self.assertEqual(self.c.total_rental_points(), 4)

        # Add a regular rental (5 days)
        self.c.add_rental(Rental(self.regular_movie, 5))
        self.assertEqual(self.c.total_rental_points(), 5)

        # Add a children's rental (2 days)
        self.c.add_rental(Rental(self.childrens_movie, 2))
        self.assertEqual(self.c.total_rental_points(), 6)
