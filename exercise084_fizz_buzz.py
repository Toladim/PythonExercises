# Napisz funkcję, która wypisuje liczby od 1 do N, zastępując wielokrotności 3 słowem "Fizz",
# wielokrotności 5 słowem "Buzz", a wielokrotności 3 i 5 jednocześnie słowem "FizzBuzz" 
# (klasyczny problem FizzBuzz).
# Przykład wywołania: fizz_buzz(15) 
# Wynik: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

def fizz_buzz(num: int) -> list[str]:
    for n in range(1, num + 1):
        print(n)

print(fizz_buzz(15))
