def remove_nonints(nums):
    new_list = []
    for i in range(0, len(nums)):
        if type(nums[i]) == int:
            new_list.append(nums[i])
    
    return new_list
