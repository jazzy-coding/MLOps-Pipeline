def square_root(x):
    """Calculate the square root of a number."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5
