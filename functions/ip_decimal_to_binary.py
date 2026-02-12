"""Convert a dotted-decimal IP string to dotted binary octets.

Example: '192.168.1.1' -> '11000000.10101000.00000001.00000001'

Args:
    ip_str (str): Dotted-decimal IP address.

Returns:
    str: Dotted binary octets, each zero-padded to 8 bits.
"""
def ip_decimal_to_binary(ip_str):
    from functions.validators import parse_ip_components

    octets = parse_ip_components(ip_str, base=10)
    binary_octets = [bin(o)[2:].zfill(8) for o in octets]
    return '.'.join(binary_octets)