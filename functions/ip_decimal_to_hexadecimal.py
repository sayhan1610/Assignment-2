def ip_decimal_to_hexadecimal(ip_str):
    octets = ip_str.split('.')
    hex_octets = [hex(int(octet))[2:].zfill(2).upper() for octet in octets]
    return '.'.join(hex_octets)