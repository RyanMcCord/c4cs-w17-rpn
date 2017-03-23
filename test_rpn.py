import unittest
import rpn
from colorconsole import terminal

screen = terminal.get_terminal(conEmu=False)



class TestBasics(unittest.TestCase):

	
	def test_add(self):
		screen.cprint(10, 0, "Let's test our addition:\n")
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
		screen.cprint(10, 0, "Our result to 1 + 1 is: " + str(result) + "\n")
		screen.cprint(10, 0, "------------------------\n")

	
	def test_subtract(self):
		screen.cprint(4, 0, "Let's test our subtraction:\n")
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
		screen.cprint(4, 0, "Our result to 5 - 3 is: " +  str(result) + "\n")
		screen.cprint(4, 0, "------------------------\n")

	
	def test_exponentiation(self):
		screen.cprint(3, 0, "Let's test our exponents:\n")
		result = rpn.calculate('4 2 ^')
		self.assertEqual(16, result)
		screen.cprint(3, 0, "Our result to 4 ^ 2 is: " +  str(result) + "\n")
		screen.cprint(3, 0, "------------------------\n")

	
	def test_multiply(self):
		screen.cprint(13, 0, "Let's test our multiplication:\n")
		result = rpn.calculate('8 4 *')
		self.assertEqual(32, result)
		screen.cprint(13, 0, "Our result to 8 * 4 is: " +  str(result) + "\n")
		screen.cprint(13, 0, "------------------------\n")


	def test_divide(self):
		screen.cprint(14, 0, "Let's test our division:\n")
		result = rpn.calculate('8 4 /')
		self.assertEqual(2, result)
		screen.cprint(14, 0, "Our result to 8 / 4 is: " +  str(result) + "\n")
		screen.cprint(14, 0, "------------------------\n")
	screen.reset_colors()
