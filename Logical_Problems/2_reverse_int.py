'''
2.Reverse Integer:
Input= 123
output: 321
Input: -4576
output: -6754
'''

def reverse_int(n):
    negative = n<0

    n = str(abs(n))[::-1]
    reverse_num = int(n)

    if negative: 
        reverse_num = - reverse_num
    return reverse_num

print(reverse_int(321))
print(reverse_int(-321))