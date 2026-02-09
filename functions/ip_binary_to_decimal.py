def ip_binary_to_decimal(ip_binary_str):
    binary_octets = ip_binary_str.split('.')
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    return '.'.join(decimal_octets)