# 2. Check if string starts with 'Hello'

import re

text = "Hello world!"
if re.match(r'^Hello', text):
    print("Starts with Hello")
else:
    print("Does not start with Hello")