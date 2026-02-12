"""Convert a hexadecimal string to its decimal integer value.

Args:
    hex_str (str): Hex string like 'FF' or '0F'.

Returns:
    int: Decimal integer parsed from hex.
"""
def hexadecimal_to_decimal(hex_str):
    # int with base 16 parses hexadecimal strings
    return int(hex_str, 16)