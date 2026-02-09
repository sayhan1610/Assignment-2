def ip_decimal_to_binary(ip_str):
    octets = ip_str.split('.')
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return '.'.join(binary_octets)