'''
23. find the fibonacci series
'''

def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        x = recur_fibonacci(n-1) + recur_fibonacci(n-2)
        return x  

n_terms = int(input("enter the no. of terms: "))

def fibonacci(n_terms):
    i = 1
    while i <= n_terms:
        if n_terms <= 0:
            print("please enter a positive integer: ")
        else:
            print(recur_fibonacci(i))
            i+=1

print(fibonacci(n_terms))


#          or

def fib(n ,num1 = 0 , num2 = 1 , count = 1):
    if n < count:
        return 
    print(num1, end=" ")
    fib(n , num1 = num2 , num2 = num1+num2 , count = count+1)
   

n = int(input())
fib(n)


# print the nth fibonacci term

def fibo(n_terms):
    if n_terms <= 0:
        return 0
    elif n_terms == 1:
        return 0
    elif n_terms == 2:
        return 1
    else:
        return (fibo(n_terms-1) + fibo(n_terms-2))


n_terms = int(input("enter the nth terms: "))
print(fibo(n_terms))