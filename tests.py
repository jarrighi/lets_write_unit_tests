import unittest
import sys
from pokedex import *

class SpeciesTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_create_pokemon_object(self):
		pass

	def test_catch_prints_success_message(self):
		pass

	def test_lookup_prints_error_message(self):
		pass

	def test_catch_errors_on_non_string_input(self):
		pass

	def test_catch_errors_on_bad_name_input(self):
		pass


if __name__ == "__main__":
	unittest.main(buffer=True) # buffer=True so print statements can be collected