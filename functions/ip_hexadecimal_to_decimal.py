"""Convert dotted hexadecimal IP octets to dotted decimal octets.

Args:
    ip_hex_str (str): Dotted hexadecimal octets separated by '.'.

Returns:
    str: Dotted decimal IP address.
"""
def ip_hexadecimal_to_decimal(ip_hex_str):
    from functions.validators import parse_ip_components

    octets = parse_ip_components(ip_hex_str, base=16)
    decimal_octets = [str(o) for o in octets]
    return '.'.join(decimal_octets)