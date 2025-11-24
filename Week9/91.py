def find_min_max(*nums):
    if not nums:
        return None, None
    min_val = max_val = nums[0]
    for n in nums:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
    return min_val, max_val

a, b = find_min_max(10, 25, 5, 30, 12, 8)
print("Minimum:", a)
print("Maximum:", b)
