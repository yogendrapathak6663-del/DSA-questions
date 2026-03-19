from collections import Counter

def count_frequency(arr):
    freq = Counter(arr)
    for num, count in sorted(freq.items()):
        print(f"{num} occurs {count} times")

count_frequency([1,2,3,3,4,1,4,5,1,2])
