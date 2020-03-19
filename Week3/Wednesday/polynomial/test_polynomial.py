import unittest
from polynomial import Term, Polynomial, Derivative

class TestTerm(unittest.TestCase):
	def test_initializing_of_term(self):
		term = Term('x^3')

		self.assertTrue(getattr((term),'coef') == 1)
		self.assertTrue(getattr((term),'pow') == 3)


	def test_eq_dunder(self):
		term1 = Term('2x^3')
		term2 = Term('2x^3')

		self.assertTrue(term1 == term2)

	def test_get_derivative_of_constant(self):
		term = Term('3')

		self.assertTrue(term.get_derivative() == 0)

	def test_get_derivative_of_x_on_power_one(self):
		term = Term('3x')

		self.assertTrue(term.get_derivative() == 3)

	def test_get_derivative_with_power_bigger_than_one(self):
		term = Term('3x^2')

		# also works 3x^2 == 6x^1
		self.assertTrue(term.get_derivative() == Term('6x'))

if __name__ == '__main__':
	unittest.main()