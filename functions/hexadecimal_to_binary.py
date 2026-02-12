"""Convert a hexadecimal string to a binary string (no '0b').

Args:
    hex_str (str): Hex string like 'A' or '0A'.

Returns:
    str: Binary string representation without '0b'.
"""
def hexadecimal_to_binary(hex_str):
    # int(..., 16) parses hex; bin() converts back to binary string
    decimal = int(hex_str, 16)
    return bin(decimal)[2:]