def ip_hexadecimal_to_decimal(ip_hex_str):
    hex_octets = ip_hex_str.split('.')
    decimal_octets = [str(int(octet, 16)) for octet in hex_octets]
    return '.'.join(decimal_octets)