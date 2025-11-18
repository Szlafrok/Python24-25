def rgb_to_hsv(r, g, b):
    r, g, b = r / 255, g / 255, b / 255

    c_max = max(r, g, b)  
    c_min = min(r, g, b)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    elif c_max == b:
        h = 60 * (((r - g) / delta) + 4)

    s = 0 if c_max == 0 else delta / c_max

    v = c_max

    return h, s, v

print(rgb_to_hsv(255, 255, 255))