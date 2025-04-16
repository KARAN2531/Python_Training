'''
13.Given a sorted integer array and a target, determine if the target exists in the
array in logarithmic time. If a target exists in the array, the procedure should
return the index of it.

Input: nums[] = [2, 3, 5, 7, 9], target = 7
Output: 3
Explanation: Element found at 4th (index 3) position

• If there are duplicate elements in the array, the procedure may return any index whose element is
equal to the target.
Input: nums[] = [1, 2, 3, 4, 4, 5, 6, 7], target = 4
'''
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Found
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Not found