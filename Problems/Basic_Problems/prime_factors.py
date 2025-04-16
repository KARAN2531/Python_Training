'''
6. Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N.'''

def isPrime(n):
    for i in range(2, (n//2)+1):
        if n%i==0:
            return False
    
    return True

n = int(input("Enter a number : "))
lst=[]
for i in range (2, (n//2)+1):
    if n%i==0 and isPrime(i):
        lst.append(i)
    
print(lst)