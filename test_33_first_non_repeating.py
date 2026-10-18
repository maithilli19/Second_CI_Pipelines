import importlib

module = importlib.import_module("33_first_non_repeating")
first_non_repeating_char = module.first_non_repeating_char

def test_first_non_repeating_basic():
    assert first_non_repeating_char("swiss") == "w"

def test_first_non_repeating_none():
    assert first_non_repeating_char("aabbcc") is None

def test_first_non_repeating_empty():
    assert first_non_repeating_char("") is None