def true_int(char: str) -> int: # 0-9 -> 9, A -> 10, B -> 11, ..., F -> 15
    if char.isdigit():
        return int(char)
    return ord(char) - ord("A") + 10

def true_char(n: int) -> str: # funkcja odwrotna do true_int
    if n >= 10:
        return chr(n + ord("A") - 10)
    return str(n)

def to_decimal(n: str, p: int) -> int: # Konwersja z dowolnego systemu na dziesiętny
    n = n.upper()
    res = 0
    mult = 1
    for char in n[::-1]:
        res += mult * true_int(char)
        mult *= p
    return res

def from_decimal(n: int, p: int) -> str: # Konwersja z systemu dziesiętnego na dowolny
    res = ""
    while n > 0:
        res += true_char(n % p)
        n //= p
    return res[::-1]

def hex_piece(hex: str) -> str:
    return "0" + hex if len(hex) == 1 else hex

def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    if len(hex) == 7:
        hex = hex[1:] # jeśli na początku jest "#"
    return (to_decimal(hex[0:2], 16), to_decimal(hex[2:4], 16), to_decimal(hex[4:6], 16))

def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    code = "#"
    code += hex_piece(from_decimal(r, 16))
    code += hex_piece(from_decimal(g, 16))
    code += hex_piece(from_decimal(b, 16))
    return code

print(hex_to_rgb("#28A2F9"))
print(rgb_to_hex((40, 162, 249)))