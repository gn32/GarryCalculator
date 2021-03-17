import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_addition_method_calculator(self):
        self.assertEqual(self.calculator.add(3, 2), 5)

    def test_subtraction_method_calculator(self):
        self.assertEqual(self.calculator.sub(5, 2), 3)

    def test_multiplication_method_calculator(self):
       self.assertEqual(self.calculator.mul(3, 3), 9)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.div(4, 2), 2)


    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.sq(5), 25)


    def test_squareroot_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(16), 4)


if __name__ == '__main__':
      unittest.main()