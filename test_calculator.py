import unittest
import rpncalc

class TestCalc(unittest.TestCase):
	def test_calc_addition(self):
		expression = "4 6 +"
		actual = rpncalc.calc(expression)
		expected = 10
		self.assertEqual(actual, expected)
	def test_calc_subtraction(self):
		expression = "4 6 -"
		actual = rpncalc.calc(expression)
		expected = -2
		self.assertEqual(actual, expected)
	def test_calc_multiplication(self):
		expression = "4 6 *"
		actual = rpncalc.calc(expression)
		expected = 24
		self.assertEqual(actual, expected)
	def test_calc_division(self):
		expression = "81 9 /"
		actual = rpncalc.calc(expression)
		expected = 9
		self.assertEqual(actual, expected)
	def test_calc_modulo(self):
		expression = "80 9 %"
		actual = rpncalc.calc(expression)
		expected = 8
		self.assertEqual(actual, expected)
	def test_calc_complex(self):
		expression = "70 5 + 4 2 / *"
		actual = rpncalc.calc(expression)
		expected = 150
		self.assertEqual(actual, expected)
	def test_calc_invalid_expression(self):
		expression = "80 9"
		actual = rpncalc.calc(expression)
		expected = Exception
		self.assertEqual(actual, expected)
	def test_calc_invalid_symbols(self):
		expression = "test"
		actual = rpncalc.calc(expression)
		expected = ValueError
		self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()