def ip_binary_to_hexadecimal(ip_binary_str):
    binary_octets = ip_binary_str.split('.')
    hex_octets = [hex(int(octet, 2))[2:].zfill(2).upper() for octet in binary_octets]
    return '.'.join(hex_octets)