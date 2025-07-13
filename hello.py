"""Module for mathematical operations."""

def square_root(x: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        x (float): The number to calculate the square root of.

    Returns:
        float: The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5
