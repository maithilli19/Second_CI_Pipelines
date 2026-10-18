def count_words(sentence: str) -> int:
    """
    Counts the number of words in a given sentence.
    """
    if not sentence or not sentence.strip():
        return 0
    return len(sentence.strip().split())