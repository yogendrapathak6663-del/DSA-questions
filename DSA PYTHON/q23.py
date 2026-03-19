def count_pairs_with_sum(arr, target):
    count = 0
    seen = {}
    for num in arr:
        complement = target - num
        count += seen.get(complement, 0)
        seen[num] = seen.get(num, 0) + 1
    return count
