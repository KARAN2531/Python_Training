'''3. Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.'''

def check_leap_year(n):
    
    if (n<1000 or n>9999):
        print("Invalid Input!")
    elif ((n%4 == 0 and n%100 != 0) or ( n%400 == 0)):
        print("Leap Year")
    else:
        print("Not a leap Year")
n = int(input())
check_leap_year(n)
    

    