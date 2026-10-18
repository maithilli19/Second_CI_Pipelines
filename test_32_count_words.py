import importlib

word_module = importlib.import_module("32_count_words")
count_words = word_module.count_words

def test_count_words_standard():
    assert count_words("Hello world from Python") == 4

def test_count_words_empty():
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_count_words_extra_spaces():
    assert count_words("  Data   Structures  ") == 2