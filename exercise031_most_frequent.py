# Napisz funkcję most_frequent(), która przyjmie listę liczb całkowitych i zwróci liczbę,
# która występuje najczęściej.
# Jeśli kilka liczb występuje równie często – zwróć dowolną z nich.

def most_frequent(numbers: list[int]) -> int:
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    return max(counts, key=counts.get)

    

print(most_frequent([1, 2, 2, 3, 32, 3, 1, 32, 1, 1, 1]))