def first_non_repeating_char(s: str) -> str:
    """
    Finds the first non-repeating character in a string.
    Returns the character, or None if all characters repeat or string is empty.
    """
    if not s:
        return None
        
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    for char in s:
        if char_counts[char] == 1:
            return char
            
    return None