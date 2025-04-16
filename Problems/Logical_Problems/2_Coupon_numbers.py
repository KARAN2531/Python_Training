'''2. Coupon Numbers
a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
process distinct coupons.
'''
import random

class CouponCollector:
    @staticmethod
    def generate_coupon(n):
        return random.randint(1, n)

    @staticmethod
    def collect_coupons(n):
        collected = set()
        total_random_numbers = 0
        while len(collected) < n:
            coupon = CouponCollector.generate_coupon(n)
            collected.add(coupon)
            total_random_numbers += 1
        return total_random_numbers

N = int(input("Enter the number of distinct coupon numbers: "))
random_count = CouponCollector.collect_coupons(N)

print(f"Total random numbers needed to collect {N} distinct coupons: {random_count}")
  