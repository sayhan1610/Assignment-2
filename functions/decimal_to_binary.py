"""Convert an integer decimal to its binary string representation.

Args:
    decimal (int): Decimal integer value.

Returns:
    str: Binary string without '0b' prefix.
"""
def decimal_to_binary(decimal):
    # bin() returns '0b...' — strip the '0b' prefix
    return bin(decimal)[2:]