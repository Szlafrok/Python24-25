import numpy as np

# Zadanie 1
def most_char(string):
    return max([(string.count(char), char) for char in string])[1]
    # Bardzo sprytnie! 1 / 1
    # Chociaż trochę niewydajne, bo wywołujesz count n razy (gdzie n = len(string))
    # W rezultacie wykonujesz n**2 operacji. Rozwiązanie bazujące na np. słowniku
    # z licznikami wykonywałoby w przybliżeniu n operacji
    # https://www.algorytm.edu.pl/matura-informatyka/zlozonosc-algorytmu
string = "akewaivmknak"
print(most_char(string))

# Zadanie 2
def sort_second_elem(data):
    return sorted(data, key=lambda data: data[1])

    # Bomba: 1.5 / 1.5

data = [(1, 5, 3), (4, 2, 2), (6, 9, 0)]
print(sort_second_elem(data))

# Zadanie 3
def srednia_geometryczna(liczby):
    iloczyn = np.prod(liczby)
    srednia = np.power(iloczyn, 1/len(liczby)) # Super! 1 / 1
    return srednia

liczby = [1, 2, 3, 4, 5]
print(srednia_geometryczna(liczby))

# Zadanie 4
def prime_gen():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

gen = prime_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # Bardzo eleganckie :) 1.5 / 1.5

# Zadanie 5
# Dekorator: dodaje funkcjonalność do funkcji bez zmieniania jej kodu

# 1 / 1



# Σ 6 / 6 ;)