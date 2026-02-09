def rgb_hexadecimal_to_binary(rgb_hex_str):
    r_hex, g_hex, b_hex = rgb_hex_str.split(',')
    r = int(r_hex, 16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)
    return f"{bin(r)[2:].zfill(8)},{bin(g)[2:].zfill(8)},{bin(b)[2:].zfill(8)}"