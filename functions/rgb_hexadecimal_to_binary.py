"""Convert RGB hex components to 8-bit binary component strings.

Example: 'FF,00,00' -> '11111111,00000000,00000000'

Args:
    rgb_hex_str (str): Comma-separated hex values for R,G,B.

Returns:
    str: Comma-separated 8-bit binary strings.
"""
def rgb_hexadecimal_to_binary(rgb_hex_str):
    from functions.validators import parse_rgb_components

    r, g, b = parse_rgb_components(rgb_hex_str, base=16)
    return f"{bin(r)[2:].zfill(8)},{bin(g)[2:].zfill(8)},{bin(b)[2:].zfill(8)}"