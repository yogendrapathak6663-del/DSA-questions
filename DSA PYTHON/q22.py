def max_product_subarray(nums):
    max_prod, min_prod, result = nums[0], nums[0], nums[0]
    
    for i in range(1, len(nums)):
        temp_max = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        min_prod = min(nums[i], max_prod * nums[i], min_prod * nums[i])
        max_prod = temp_max
        result = max(result, max_prod)
    
    return result
