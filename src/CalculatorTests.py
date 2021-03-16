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
        print('hi')
        calculator = Calculator()
        self.assertEqual(calculator.add(3, 2), 5)

if __name__ == '__main__':
      unittest.main()