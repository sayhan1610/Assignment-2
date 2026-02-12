"""Convert RGB decimal components to binary strings (8 bits each).

Example: '255,0,0' -> '11111111,00000000,00000000'

Args:
    rgb_str (str): Comma-separated decimal R,G,B values.

Returns:
    str: Comma-separated 8-bit binary strings for R,G,B.
"""
def rgb_decimal_to_binary(rgb_str):
    from functions.validators import parse_rgb_components

    r, g, b = parse_rgb_components(rgb_str, base=10)
    return f"{bin(r)[2:].zfill(8)},{bin(g)[2:].zfill(8)},{bin(b)[2:].zfill(8)}"