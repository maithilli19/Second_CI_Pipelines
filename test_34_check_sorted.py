import importlib

module = importlib.import_module("34_check_sorted")
is_sorted = module.is_sorted

def test_is_sorted_true():
    assert is_sorted([1, 2, 3, 4, 5]) is True

def test_is_sorted_false():
    assert is_sorted([1, 3, 2, 4]) is False

def test_is_sorted_single_or_empty():
    assert is_sorted([42]) is True
    assert is_sorted([]) is True
    