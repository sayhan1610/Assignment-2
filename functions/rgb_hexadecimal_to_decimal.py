"""Convert RGB hex components to decimal components.

Example: 'FF,00,00' -> '255,0,0'

Args:
    rgb_hex_str (str): Comma-separated hex values for R,G,B.

Returns:
    str: Comma-separated decimal values for R,G,B.
"""
def rgb_hexadecimal_to_decimal(rgb_hex_str):
    from functions.validators import parse_rgb_components

    r, g, b = parse_rgb_components(rgb_hex_str, base=16)
    return f"{r},{g},{b}"