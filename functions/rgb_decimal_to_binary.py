def rgb_decimal_to_binary(rgb_str):
    r, g, b = map(int, rgb_str.split(','))
    return f"{bin(r)[2:].zfill(8)},{bin(g)[2:].zfill(8)},{bin(b)[2:].zfill(8)}"