"""Convert dotted hexadecimal IP octets to dotted binary octets.

Example: 'C0.A8.01.01' -> '11000000.10101000.00000001.00000001'

Args:
    ip_hex_str (str): Dotted hex octets separated by '.'.

Returns:
    str: Dotted binary octets, each zero-padded to 8 bits.
"""
def ip_hexadecimal_to_binary(ip_hex_str):
    from functions.validators import parse_ip_components

    octets = parse_ip_components(ip_hex_str, base=16)
    binary_octets = [bin(o)[2:].zfill(8) for o in octets]
    return '.'.join(binary_octets)