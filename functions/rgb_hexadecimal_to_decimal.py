def rgb_hexadecimal_to_decimal(rgb_hex_str):
    r_hex, g_hex, b_hex = rgb_hex_str.split(',')
    r = int(r_hex, 16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)
    return f"{r},{g},{b}"