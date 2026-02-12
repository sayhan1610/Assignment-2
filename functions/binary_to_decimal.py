"""Convert a binary string to its decimal integer value.

Args:
    binary_str (str): Binary string like '1010'.

Returns:
    int: Decimal representation of the binary string.
"""
def binary_to_decimal(binary_str):
    # Use Python's built-in int conversion with base 2
    return int(binary_str, 2)