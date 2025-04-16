'''
16.Given three lists of integers: lst1, lst2, lst3, return the sum of integers which
are common in all three lists.
Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.
sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
// 2, 2 & 3 are common in all 3 lists.

sum_common([1], [1], [2]) ➞ 0
'''

lst1 = list(map(int, input("Enter elements of list 1: "). split()))
lst2 = list(map(int, input("Enter elements of list 2: "). split()))
lst3 = list(map(int, input("Enter elements of list 3: "). split()))

def sum_common(lst1, lst2, lst3):
    s1 = set(lst1)
    s2 = set(lst2)
    s3 = set(lst3)

    set1 = s1.intersection(s2)
    output_set = s3.intersection(set1)
    output = list(output_set)

    result = sum(output)

    return result

print("output: ", sum_common(lst1, lst2, lst3))