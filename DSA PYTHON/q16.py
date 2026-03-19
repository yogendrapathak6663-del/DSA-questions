def find_kth_largest(nums, k):
    return sorted(nums, reverse=True)[k-1]

print(find_kth_largest([3,2,1,5,6,4], 2))  # 5
