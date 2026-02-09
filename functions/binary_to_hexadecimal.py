def binary_to_hexadecimal(binary_str):
    decimal = int(binary_str, 2)
    return hex(decimal)[2:].upper()