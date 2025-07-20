# Napisz funkcję, która wypisuje liczby od 1 do N, zastępując wielokrotności 3 słowem "Fizz",
# wielokrotności 5 słowem "Buzz", a wielokrotności 3 i 5 jednocześnie słowem "FizzBuzz" 
# (klasyczny problem FizzBuzz).
# Przykład wywołania: fizz_buzz(15) 
# Wynik: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

def fizz_buzz(num: int) -> list[str]:
    elements = []
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            elements.append("FizzBuzz")
        elif n % 3 == 0:
            elements.append("Fizz")
        elif n % 5 == 0:
            elements.append("Buzz")
        else:
            elements.append(str(n))
    return elements


print(fizz_buzz(15))
