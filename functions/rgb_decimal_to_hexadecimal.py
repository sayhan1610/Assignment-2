def rgb_decimal_to_hexadecimal(rgb_str):
    r, g, b = map(int, rgb_str.split(','))
    return f"{hex(r)[2:].zfill(2).upper()},{hex(g)[2:].zfill(2).upper()},{hex(b)[2:].zfill(2).upper()}"