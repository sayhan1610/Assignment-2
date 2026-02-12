"""Convert an IP address with binary octets to dotted hexadecimal octets.

Example: '11000000.10101000.00000001.00000001' -> 'C0.A8.01.01'

Args:
    ip_binary_str (str): Dotted binary octets.

Returns:
    str: Dotted hexadecimal octets (uppercase), each two chars.
"""
def ip_binary_to_hexadecimal(ip_binary_str):
    from functions.validators import parse_ip_components

    octets = parse_ip_components(ip_binary_str, base=2)
    hex_octets = [hex(o)[2:].zfill(2).upper() for o in octets]
    return '.'.join(hex_octets)