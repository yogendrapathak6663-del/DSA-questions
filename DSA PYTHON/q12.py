def second_largest_smallest(arr):
    if len(arr) < 2:
        return -1, -1
    
    unique = sorted(set(arr))
    if len(unique) < 2:
        return -1, -1
    
    return unique[1], unique[-2]

arr1 = [1,2,4,7,7,5]
sec_small, sec_large = second_largest_smallest(arr1)
print(f"Second Smallest: {sec_small}, Second Largest: {sec_large}")
