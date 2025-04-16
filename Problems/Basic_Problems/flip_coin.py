'''
2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails'''

from random import uniform
def flips(n):
    heads = 0
    tails = 0

    for _ in range(n):
        x = round(uniform(0,1),1) #To generate random numbers between 0 to 1 with only 1 digit after the decimal point
        print(x)
        if x<0.5:
            tails += 1
        else:
            heads += 1
            
        
    print(f"Number of Heads: {heads}\nNumber of Tails: {tails}")
    print(f"Heads % : {(heads/n) * 100:.2f}%")
    print(f"Tails % : {(tails/n) * 100:.2f}%")
    
    
n = int(input("Enter the number of coin flips: "))
flips(n)
