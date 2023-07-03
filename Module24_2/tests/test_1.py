import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 7) == 35

    def test_division_success(self):
        assert self.calc.division(self, 33, 3) == 11

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 12, 2) == 10

    def test_adding_success(self):
        assert self.calc.adding(self, 6, 3) == 9

    def teardown(self):
        print('Выполнение метода Teardown')

