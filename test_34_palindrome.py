import importlib

module = importlib.import_module("34_palindrome")
is_palindrome = module.is_palindrome

def test_palindrome_true():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False

def test_palindrome_empty():
    assert is_palindrome("") is True