'''
8.Given a positive number, check if it is a perfect square without using any
built-in library function. A perfect square is a number that is the square of an
integer.
Input: n = 25
Output: true
Explanation: 25 is a perfect square since it can be written as 5×5.

Input: n = 20
Output: false

Explanation: 20 is not the product of an integer with itself.

'''

n = int(input("Enter your number to check if its a square: "))
x = n ** 0.5
if ((n / x) == x):
    print("True")
else:
    print("False")    