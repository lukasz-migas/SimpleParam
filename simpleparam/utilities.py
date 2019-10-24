"""Utilities"""
import numbers


def is_number(obj):
    """Check if value is a number"""
    if isinstance(obj, numbers.Number):
        return True
    # The extra check is for classes that behave like numbers, such as those
    # found in numpy, gmpy, etc.
    elif hasattr(obj, "__int__") and hasattr(obj, "__add__"):
        return True
    return False
