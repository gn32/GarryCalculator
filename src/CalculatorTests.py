import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        CsvReader.data = []

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 4)

    def test_addition(self):
        test_data = CsvReader('/src/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('/src/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('/src/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_division(self):
        test_data = CsvReader('/src/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, round(float(row['Result']),9))

    def test_square(self):
        test_data = CsvReader('/src/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sq(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squareroot(self):
        test_data = CsvReader('/src/squareroot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), round(float(row['Result']),8))
            self.assertEqual(self.calculator.result, round(float(row['Result']),8))




if __name__ == '__main__':
    unittest.main()
