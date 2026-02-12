"""Convert an RGB value expressed as binary components to decimal components.

Example: '11111111,00000000,00000000' -> '255,0,0'

Args:
    rgb_binary_str (str): Comma-separated binary strings for R,G,B.

Returns:
    str: Comma-separated decimal values for R,G,B.
"""
def rgb_binary_to_decimal(rgb_binary_str):
    from functions.validators import parse_rgb_components

    r, g, b = parse_rgb_components(rgb_binary_str, base=2)
    return f"{r},{g},{b}"