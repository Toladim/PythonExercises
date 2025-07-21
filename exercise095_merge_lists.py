# Napisz funkcję, która scala dwie posortowane listy w jedną posortowaną listę.
# Przykład wywołania: merge_lists([1, 3, 5], [2, 4, 6]) Wynik: [1, 2, 3, 4, 5, 6]
# def merge_lists(nums1: list[int], nums2: list[int]) -> list[int]:
#     return sorted(nums1 + nums2)
def merge_lists(nums1: list[int], nums2: list[int]) -> list[int]:
    i, j = 0, 0
    merged = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        return merged

print(merge_lists([1, 3, 5], [2, 4, 6]))