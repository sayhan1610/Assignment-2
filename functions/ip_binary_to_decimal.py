"""Convert an IP address represented with binary octets to decimal dots.

Example: '11000000.10101000.00000001.00000001' -> '192.168.1.1'

Args:
    ip_binary_str (str): Dotted binary octets separated by '.'.

Returns:
    str: Dotted decimal IP string.
"""
def ip_binary_to_decimal(ip_binary_str):
    from functions.validators import parse_ip_components

    octets = parse_ip_components(ip_binary_str, base=2)
    decimal_octets = [str(o) for o in octets]
    return '.'.join(decimal_octets)