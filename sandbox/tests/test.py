import unittest
import main

class TestMain(unittest.TestCase):	
	def test_do_stuff(self):
		num = 10
		result = main.do_stuff(num)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'asdfdsfsfsd'
		result = main.do_stuff(test_param)
		# self.assertTrue(isinstance(result, ValueError))
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		test_param = None
		result = main.do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')

unittest.main()