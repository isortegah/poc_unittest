import unittest

class NumbersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Antes de la prueba.")

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 2):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    def test_other(self):
        print("\nOther test")
        self.assertEqual(0,0)

    @classmethod
    def tearDownClass(cls):
        print("Final de la prueba")