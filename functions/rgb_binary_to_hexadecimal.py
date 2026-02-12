"""Convert RGB binary components to hexadecimal components.

Example: '11111111,00000000,00000000' -> 'FF,00,00'

Args:
    rgb_binary_str (str): Comma-separated binary strings for R,G,B.

Returns:
    str: Comma-separated 2-digit uppercase hex values.
"""
def rgb_binary_to_hexadecimal(rgb_binary_str):
    from functions.validators import parse_rgb_components

    r, g, b = parse_rgb_components(rgb_binary_str, base=2)
    return f"{hex(r)[2:].zfill(2).upper()},{hex(g)[2:].zfill(2).upper()},{hex(b)[2:].zfill(2).upper()}"