def find_gcd(a: int, b: int) -> int:
    """
    Finds the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)