import unittest
from algorithm import search

class TestSearch(unittest.TestCase):
	def setUp(self):
		self.array = [2, 4, 6, 8, 10]

	def test_successful(self):
		self.assertTrue(search(self.array, 4, 1))

	def test_failed(self):
		self.assertFalse(search(self.array, 5, 1))

	def test_oneNegative(self):
		self.assertFalse(search(self.array, -1, 2))

	def test_emptyArray(self):
		self.assertFalse(search([], 5, 2))
	
	def test_twoNegatives(self):
		self.assertTrue(search(self.array, -1, -2))

if __name__ == '__main__':
    unittest.main()
