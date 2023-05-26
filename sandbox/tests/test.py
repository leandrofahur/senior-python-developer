import unittest
import script


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = script.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdfdsfsfsd'
        result = script.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest.main()
