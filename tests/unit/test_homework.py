import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_abs_pos(calc): assert calc.absolute(10) == 10
def test_abs_neg(calc): assert calc.absolute(-10) == 10
def test_abs_zero(calc): assert calc.absolute(0) == 0
def test_abs_float(calc): assert calc.absolute(-1.5) == 1.5
def test_fact_zero(calc): assert calc.factorial(0) == 1
def test_fact_one(calc): assert calc.factorial(1) == 1
def test_fact_five(calc): assert calc.factorial(5) == 120
def test_fact_neg_err(calc):
    with pytest.raises(ValueError): calc.factorial(-1)
def test_fact_float_err(calc):
    with pytest.raises(TypeError): calc.factorial(1.5)
def test_fact_str_err(calc):
    with pytest.raises(TypeError): calc.factorial("5")