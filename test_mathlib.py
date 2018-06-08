import mathlib

def test_sum():
    total = mathlib.calc_sum(5, 6)
    assert total == 11

def test_product():
    total = mathlib.calc_product(5, 5)
    assert total == 25
