import importlib

module = importlib.import_module("40_gcd")
find_gcd = module.find_gcd

def test_gcd_standard():
    assert find_gcd(48, 18) == 6

def test_gcd_coprime():
    assert find_gcd(17, 13) == 1

def test_gcd_with_zero():
    assert find_gcd(5, 0) == 5