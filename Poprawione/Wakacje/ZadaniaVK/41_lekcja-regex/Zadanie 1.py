import re
from PIESELE import PIESELE

def bajtek_szuka_pieseli(PIESELE: list) -> list:
    pattern = r"\d{5}-\d{6}[a-zA-Z]"
    res = []
    for piesel in PIESELE:
        matches = re.findall(pattern, piesel)
        for m in matches:
            suma1 = sum(int(c) for c in m[:5])
            suma2 = sum(int(c) for c in m[6:12])
            res.append((m, suma1 == suma2))
    return res

wyn = bajtek_szuka_pieseli(PIESELE)

for w in wyn:
    print(w)

# Rozwiązanie bezbłędne. Dobrze przygotowane dane testowe!

# 5p / 3p