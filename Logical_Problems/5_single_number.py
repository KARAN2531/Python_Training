'''
5. Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,1]
Output: 1
Input: nums = [4,1,2,1,2]
Output: 4
'''

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result    

nums = list(map(int, input("Enter numbers seperated by spaces: ").split()))
print(single_number(nums))