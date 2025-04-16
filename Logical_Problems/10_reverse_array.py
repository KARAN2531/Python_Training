'''
10.Given an integer array, in-place reverse it without using any inbuilt functions.
Input : [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
'''

input_array = list(map(int, input("Enter number separated by spaces: ").split(" ")))
result = input_array[::-1]
print(result)