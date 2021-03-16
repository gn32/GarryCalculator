import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)

    def test_addition_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(3, 2), 5)

    def test_subtraction_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sub(5, 2), 3)

    def test_multiplication_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.mul(3, 3), 9)

    def test_division_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.div(4, 2), 2)



if __name__ == '__main__':
      unittest.main()