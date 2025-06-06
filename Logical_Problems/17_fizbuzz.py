'''
17.Create a function that takes a number as an argument and returns "Fizz",
"Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the
examples below.
The output should always be a string eve=n if it is not a multiple of 3 or 5.

Examples
fizz_buzz(3) ➞ "Fizz"
fizz_buzz(5) ➞ "Buzz"
fizz_buzz(15) ➞ "FizzBuzz"
'''

def fizz_buzz(n):
    if n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    elif n%3 == 0 and n%5 == 0:
        print("FizzBuzz")