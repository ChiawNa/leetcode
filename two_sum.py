#https://leetcode.com/problems/two-sum/description/

#easy version
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            return []
            
# Example usage:
nums = [2, 7, 11, 15]
target = 17
print(two_sum(nums, target))  
# Output: [0, 1] (since nums[0] + nums[1] = 2 + 7 = 9)


#hard version
def twoSum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

#hai