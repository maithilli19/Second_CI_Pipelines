def move_zeros_to_end(lst: list) -> list:
    """
    Moves all zeros to the end of the list while maintaining the relative order of non-zero elements.
    """
    if not lst:
        return []
        
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros