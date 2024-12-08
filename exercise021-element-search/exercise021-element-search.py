"""Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
an appropriate boolean.

Extras:

1.Use binary search."""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


exemple = [1, 3, 5, 30, 42, 43, 500]
print(binary_search(exemple, 5))