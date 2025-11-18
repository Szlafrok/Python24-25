import rok

def test_rok():
    assert rok.rok_przestepny(2024) == True
    assert rok.rok_przestepny(2023) == False
    assert rok.rok_przestepny(2000) == True
    assert rok.rok_przestepny(1900) == False
    assert rok.rok_przestepny(1754) == False

# Super!

# 3 / 3