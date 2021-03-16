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
        self.assertEqual(calculator.sub(3, 2), 1)


if __name__ == '__main__':
      unittest.main()