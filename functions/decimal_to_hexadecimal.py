"""Convert an integer decimal to its hexadecimal string (uppercase).

Args:
    decimal (int): Decimal integer value.

Returns:
    str: Hex string without '0x' prefix, uppercase.
"""
def decimal_to_hexadecimal(decimal):
    # hex() -> '0x..', strip prefix and uppercase
    return hex(decimal)[2:].upper()