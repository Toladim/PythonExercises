# Napisz funkcję, która oblicza tzw. cyfrowy rdzeń (digital root) danej liczby. 
# Sumuj cyfry liczby, a następnie sumuj cyfry wyniku, powtarzając ten proces, aż zostanie jedna cyfra.
# Przykład wywołania: digital_root(789) Wynik: 6 (ponieważ 7+8+9=24, a 2+4=6)

def digital_root(num: int) -> int:
    if num < 10:
        return num
    else:
        result = sum(int(n) for n in str(num))
        return digital_root(result)

print(digital_root(789))

        
    