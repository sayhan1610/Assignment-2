"""Convert a binary string to a hexadecimal string (uppercase, no prefix).

Args:
    binary_str (str): Binary string like '11111111'.

Returns:
    str: Hexadecimal string like 'FF'.
"""
def binary_to_hexadecimal(binary_str):
    # Convert binary -> decimal, then decimal -> hex string
    decimal = int(binary_str, 2)
    # hex() returns '0x..' so strip prefix and uppercase
    return hex(decimal)[2:].upper()