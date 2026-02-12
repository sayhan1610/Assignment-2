"""Validation helpers for IP and RGB conversion functions.

Provides parsing and validation for dotted IP and comma-separated RGB
components across binary/decimal/hex bases, enforcing 0-255 limits.
"""
def parse_components(value_str, sep, count, base):
    parts = [p.strip() for p in value_str.split(sep)]
    if len(parts) != count:
        raise ValueError(f"Expected {count} components separated by '{sep}'")

    vals = []
    for p in parts:
        if base == 2:
            if not p or any(ch not in '01' for ch in p):
                raise ValueError(f"Invalid binary component: {p}")
            if len(p) > 8:
                raise ValueError(f"Binary component too long (max 8 bits): {p}")
        elif base == 16:
            if not p:
                raise ValueError(f"Invalid hexadecimal component: {p}")
            if len(p) > 2:
                raise ValueError(f"Hex component too long (max 2 chars): {p}")

        try:
            val = int(p, base)
        except Exception:
            raise ValueError(f"Invalid base-{base} component: {p}")

        if not (0 <= val <= 255):
            raise ValueError(f"Component out of range 0-255: {p}")

        vals.append(val)

    return vals


def parse_ip_components(value_str, base):
    return parse_components(value_str, '.', 4, base)


def parse_rgb_components(value_str, base):
    return parse_components(value_str, ',', 3, base)
