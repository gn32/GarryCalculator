from addition import addition
from subtraction import subtraction
from multiplication import multiplication

class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result = x;
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def mul(self, a, b):
        self.result = multiplication(a,b)
        return self.result

