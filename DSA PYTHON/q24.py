def move_zeros_to_end(nums):
    nonzero_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonzero_idx], nums[i] = nums[i], nums[nonzero_idx]
            nonzero_idx += 1
