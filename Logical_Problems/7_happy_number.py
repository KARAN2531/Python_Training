'''
7.Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
Explanation:
1
2 + 9
2 = 82
8
2 + 2
2 = 68
6
2 + 8
2 = 100
1
2 + 0
2 + 0
2 = 1

Input: n = 2
Output: false
'''

def is_happy(n):
    known = set()
    
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n)) 

        if n in known:
            return False
        
        known.add(n)
    
    return True  

n = int(input("Enter number to check if happy or not: "))

if is_happy(n):
    print("True")
else:
    print("False")
