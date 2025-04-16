'''
4.Given an array nums, write a function to move all zeroes to the end of it while
maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]

Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
'''

def move_zeroes(nums):
    num_output = []

    for num in nums:
        if num!=0:
            num_output.append(num)

    num_output.extend([0] * (len(nums) - len(num_output))) 

    return num_output  

nums = list(map(int, input("Enter integers seperated by space: ").split()))

result = move_zeroes(nums)
print(result)