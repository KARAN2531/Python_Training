'''
5. Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.'''

def harmonic(n):
    sum = 0
    for i in range (1, n+1):
        sum += (1/i)
    return sum

n =int(input("Enter the last number: "))
print(f"Harmonic Sum: {harmonic(n)}")