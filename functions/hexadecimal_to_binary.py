def hexadecimal_to_binary(hex_str):
    decimal = int(hex_str, 16)
    return bin(decimal)[2:]