def find_min(nums):
    min = nums[0]
    for i in range(0, len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min
