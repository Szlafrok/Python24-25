def rok_przestepny(rok: int) -> bool:
    return rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0)