'''1.Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def two_sums(nums, target):

    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []    

nums = list(map(int, input("Enter the numbers seperated b spaces: ").split()))   
target = int(input("Enter your target: "))     

result = two_sums(nums, target)
print("Indices: ", result)
