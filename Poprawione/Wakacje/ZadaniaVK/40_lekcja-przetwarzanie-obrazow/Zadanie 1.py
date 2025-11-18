def hsv_to_rgb(h, s, v):
    c = h * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r1, g1, b1 = c, x, 0
    elif 60 <= h < 120:
        r1, g1, b1 = x, c, 0
    elif 120 <= h < 180:
        r1, g1, b1 = 0, c, x
    elif 180 <= h < 240:
        r1, g1, b1 = 0, x, c
    elif 240 <= h < 300:
        r1, g1, b1 = x, 0, c
    elif 300 <= h < 360:
        r1, g1, b1 = c, 0, x
    else:
        r1, g1, b1 = 0, 0, 0

    r = int((r1 + m) * 255)
    g = int((g1 + m) * 255)
    b = int((b1 + m) * 255)

    return r, g, b

print(hsv_to_rgb(40, 0, 0.5))

# W zadaniu trzeba było przekonwertować HEX, nie HSV :(
# Przez chwilę czytałem kod i zastanawiałem się, czemu tak dołożyłeś sobie pracy :(