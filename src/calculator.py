import math

class Calculator:
    def absolute(self, number):
        return abs(number)

    def factorial(self, n):
        if not isinstance(n, int):
            raise TypeError("Value must be an integer")
        if n < 0:
            raise ValueError("Value cannot be negative")
        return math.factorial(n)