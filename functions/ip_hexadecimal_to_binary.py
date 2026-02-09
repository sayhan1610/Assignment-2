def ip_hexadecimal_to_binary(ip_hex_str):
    hex_octets = ip_hex_str.split('.')
    binary_octets = [bin(int(octet, 16))[2:].zfill(8) for octet in hex_octets]
    return '.'.join(binary_octets)