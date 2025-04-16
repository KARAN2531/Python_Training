#1. Find all numbers in a string 

import re

text = "I have 2 apples and 3 bananas."
numbers = re.findall(r'\d+', text)
print(numbers)  # ['2', '3']