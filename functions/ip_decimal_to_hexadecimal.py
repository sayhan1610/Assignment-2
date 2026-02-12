"""Convert dotted-decimal IP string to dotted hexadecimal octets.

Example: '192.168.1.1' -> 'C0.A8.01.01'

Args:
    ip_str (str): Dotted-decimal IP address.

Returns:
    str: Dotted hexadecimal octets (uppercase), each 2 characters.
"""
def ip_decimal_to_hexadecimal(ip_str):
    from functions.validators import parse_ip_components

    octets = parse_ip_components(ip_str, base=10)
    hex_octets = [hex(o)[2:].zfill(2).upper() for o in octets]
    return '.'.join(hex_octets)