'''
29.Given a number, return the difference between the maximum and minimum
numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
'''

def rearranged_difference(num):
    digits = sorted(str(num))
    min_num = int("".join(digits))
    max_num = int("".join(digits[::-1]))
    return max_num - min_num

print(rearranged_difference(972882))