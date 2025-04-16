'''
4. Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.
d. O/P -> Print the year is a Leap Year or not.'''


def table_of_two(N):
    for i in range(N+1):
        p = 2*i
        print(f"2 * {i} = {p}")

N = int(input()) 
table_of_two(N)
