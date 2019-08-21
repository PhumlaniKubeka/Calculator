from MyCalculator import addition,multiply

def test_addition():
    assert addition(2,2) == 4
    assert addition(2, 3,4) == 9
    assert addition(2,3,4,5) == 13


def test_multiplyy():
    assert multiply(2,3) == 6
    assert multiply(2,3,4) == 24
    assert multiply(2,3,4,5) == 120