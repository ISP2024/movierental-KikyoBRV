import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
		self.regular_movie = Movie("Air", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", Movie.REGULAR)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		"""Test price calculation for different movie categories and rental durations"""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)

		#Test regular movie pricing
		rental = Rental(self.regular_movie,2)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie,4)
		self.assertEqual(rental.get_price(),5.0)

		#Test children's movie pricing
		rental = Rental(self.childrens_movie,3)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie,5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
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
