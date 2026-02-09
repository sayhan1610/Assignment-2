def rgb_binary_to_decimal(rgb_binary_str):
    r_bin, g_bin, b_bin = rgb_binary_str.split(',')
    r = int(r_bin, 2)
    g = int(g_bin, 2)
    b = int(b_bin, 2)
    return f"{r},{g},{b}"