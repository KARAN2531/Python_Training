'''
6.Given an array nums of size n, return the majority element.
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
nums = list(map(int, input("Enter the numbers: ").split()))

count_dict = {}

for num in nums:
    count_dict[num] = count_dict.get(num, 0) + 1

max_count = max(count_dict.values())  

for num, count in count_dict.items():
    if count == max_count:
        print(f"Number {num} has the maximum count: {count}")