def is_palindrome(s: str) -> bool:
    """
    Checks whether a given string is a palindrome 
    (reads the same forward and backward, ignoring case and spaces).
    """
    if not s:
        return True
        
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]