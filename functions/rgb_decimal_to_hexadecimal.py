"""Convert RGB decimal components to 2-digit hexadecimal components.

Example: '255,0,0' -> 'FF,00,00'

Args:
    rgb_str (str): Comma-separated decimal R,G,B values.

Returns:
    str: Comma-separated uppercase 2-char hex values.
"""
def rgb_decimal_to_hexadecimal(rgb_str):
    from functions.validators import parse_rgb_components

    r, g, b = parse_rgb_components(rgb_str, base=10)
    return f"{hex(r)[2:].zfill(2).upper()},{hex(g)[2:].zfill(2).upper()},{hex(b)[2:].zfill(2).upper()}"