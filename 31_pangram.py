import string

def is_pangram(sentence: str) -> bool:
    """
    Checks whether a given string contains every letter of the alphabet at least once.
    """
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))