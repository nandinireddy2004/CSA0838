def find_insert_position(nums, target):
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)  
nums = [1, 3, 5, 6]
target = 5
print("Output:", find_insert_position(nums, target))
nums = [1, 3, 5, 6]
target = 2
print("Output:", find_insert_position(nums, target))  
