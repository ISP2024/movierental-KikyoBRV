import unittest
from movie import Movie
from rental import Rental
from pricing import NewRelease, RegularPrice, ChildrensPrice

class PriceStrategyTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Young Woman and the Sea", 2024, ["Biography", "Drama", "Romance"])
        self.childrens_movie = Movie("Cinderella", 1950, ["Animation","Children","Musical"])
        self.regular_movie = Movie("Son of Saul", 2015, ["Drama"])

    def test_price_code_NewRelease(self):
        r = Rental(self.new_movie, 1)
        self.assertIsInstance(r.price_code, NewRelease)

    def test_price_code_ChildrensPrice(self):
        r = Rental(self.childrens_movie, 4)
        self.assertIsInstance(r.price_code, ChildrensPrice)

    def test_price_code_RegularPrice2(self):
        r = Rental(self.regular_movie, 2)
        self.assertIsInstance(r.price_code, RegularPrice)
