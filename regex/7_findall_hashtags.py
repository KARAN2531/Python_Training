# 7. Find all hashtags from a tweet

import re

tweet = "Learning #Python and #regex is fun! #100DaysOfCode"
hashtags = re.findall(r'#\w+', tweet)
print(hashtags)  # ['#Python', '#regex', '#100DaysOfCode']