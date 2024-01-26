"""
This module contains a function to calculate the largest prime factor of a given number.
"""

def largest_prime_factor(num):
    """
    Calculate the largest prime factor of the given num.

    Args:
    num (int): The num for which the largest prime factor is to be calculated.

    Returns:
    int: The largest prime factor of the given num.
    """
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            num //= factor
        else:
            factor += 1
    return num

# Example usage:
NUMBER = 600851475143
RESULT = largest_prime_factor(NUMBER)
print(RESULT)
