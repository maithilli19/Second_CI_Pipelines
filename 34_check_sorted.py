def is_sorted(lst: list) -> bool:
    """
    Checks if a given list of numbers or elements is sorted in non-decreasing order.
    """
    if not lst or len(lst) <= 1:
        return True
        
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
            
    return True