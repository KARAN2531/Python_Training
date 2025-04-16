'''
9.Given an integer array, find k'th smallest element in the array where k is a
positive integer less than or equal to the length of array.

Input : [7, 4, 6, 3, 9, 1], k = 3
Output: 4
Explanation: The 3rd smallest array element is 4

Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
Output: 4
Explanation: The 5th smallest array element is 4
'''

input_array = list(map(int, input("Enter number separated by spaces: ").split(" ")))
k = int(input("Enter the value of K: "))

result_array = sorted(input_array)
print(f"the {k}th smallest array element: ", input_array[k-1])